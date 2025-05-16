from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Pic, Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class PicUploadForm(forms.ModelForm):
    class Meta:
        model = Pic
        fields = ('image', 'caption')
        widgets = {
            'caption': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Describe tu foto…'}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'profile_pic')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tu biografía…'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': 'Escribe un comentario...',
                'class': 'comment-input'
            })
        }
