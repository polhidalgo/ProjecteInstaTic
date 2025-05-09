from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, UpdateView, CreateView, DetailView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from .forms import CustomUserCreationForm, ProfileEditForm, PicUploadForm, CommentForm
from .models import CustomUser, Pic, Follower, Like, Notification


class UserLoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        return render(request, self.template_name, {'form': form})


class UserRegisterView(View):
    template_name = 'accounts/register.html'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        # Recuento de seguidores y a quién sigue
        context['followers_count'] = user.followers.count()
        context['following_count'] = user.following.count()
        # Todas las fotos del usuario
        context['pics'] = user.pics.order_by('-created_at')
        return context

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileEditForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class PicUploadView(LoginRequiredMixin, CreateView):
    model = Pic
    form_class = PicUploadForm
    template_name = 'accounts/upload.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PicDetailView(LoginRequiredMixin, DetailView):
    model = Pic
    template_name = 'accounts/pic_detail.html'
    context_object_name = 'pic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pic = context['pic']
        context['is_liked'] = pic.likes.filter(user=self.request.user).exists()
        context['likes_count'] = pic.likes.count()
        return context

class PicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pic
    template_name = 'accounts/pic_confirm_delete.html'
    success_url = reverse_lazy('profile')

    def test_func(self):
        return self.request.user == self.get_object().user

class FeedView(LoginRequiredMixin, View):
    template_name = 'accounts/feed.html'

    def get(self, request):
        followed_users = request.user.following.values_list('followed', flat=True)
        pics = Pic.objects.filter(user__in=followed_users).order_by('-created_at')
        comment_form = CommentForm()

        # Añade flags al objeto pic para usar en plantilla
        for pic in pics:
            pic.is_liked = pic.likes.filter(user=request.user).exists()
            pic.likes_count = pic.likes.count()

        return render(request, self.template_name, {
            'pics': pics,
            'comment_form': comment_form,
        })

    def post(self, request):
        if 'pic_id' in request.POST and 'like' in request.POST:
            # Like/unlike toggle
            pic = get_object_or_404(Pic, id=request.POST.get('pic_id'))
            like, created = Like.objects.get_or_create(user=request.user, pic=pic)

            if not created:
                like.delete()
            else:
                # Notifica solo si no es tu propia foto
                if pic.user != request.user:
                    Notification.objects.create(
                        recipient=pic.user,
                        sender=request.user,
                        notification_type='like',
                        pic=pic
                    )
            return redirect('feed')

        # Comentario
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.pic_id = request.POST.get('pic_id')
            comment.save()

            # Notifica al autor de la imagen si no eres tú
            pic = comment.pic
            if pic.user != request.user:
                Notification.objects.create(
                    recipient=pic.user,
                    sender=request.user,
                    notification_type='comment',
                    pic=pic
                )

        return redirect('feed')

class UserSearchView(LoginRequiredMixin, View):
    template_name = 'accounts/user_search.html'

    def get(self, request):
        q = request.GET.get('q', '').strip()
        results = []
        if q:
            # búsqueda insensible a mayúsculas
            results = CustomUser.objects.filter(username__icontains=q)
        return render(request, self.template_name, {
            'results': results,
            'query': q,
        })

class PublicProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/public_profile.html'

    def post(self, request, username):
        profile_user = get_object_or_404(CustomUser, username=username)

        if 'follow' in request.POST:
            _, created = Follower.objects.get_or_create(
                follower=request.user,
                followed=profile_user
            )
            if created and profile_user != request.user:
                Notification.objects.create(
                    recipient=profile_user,
                    sender=request.user,
                    notification_type='follow'
                )

        elif 'unfollow' in request.POST:
            Follower.objects.filter(follower=request.user, followed=profile_user).delete()

        elif 'like' in request.POST:
            pic = get_object_or_404(Pic, id=request.POST.get('pic_id'))
            like, created = Like.objects.get_or_create(user=request.user, pic=pic)
            if not created:
                like.delete()
            else:
                if pic.user != request.user:
                    Notification.objects.create(
                        recipient=pic.user,
                        sender=request.user,
                        notification_type='like',
                        pic=pic
                    )
            return redirect('user_public_profile', username=username)

        elif 'comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.pic_id = request.POST.get('pic_id')
                comment.save()

                pic = comment.pic
                if pic.user != request.user:
                    Notification.objects.create(
                        recipient=pic.user,
                        sender=request.user,
                        notification_type='comment',
                        pic=pic
                    )

        return redirect('user_public_profile', username=username)

class NotificationListView(LoginRequiredMixin, View):
    template_name = 'accounts/notifications.html'

    def get(self, request):
        notifications = request.user.notifications.order_by('-created_at')
        return render(request, self.template_name, {'notifications': notifications})
