from django.urls import path
from .views import UserLoginView, UserRegisterView, ProfileView, ProfileEditView, PicUploadView, PicDetailView, \
    PicDeleteView, FeedView, UserSearchView, PublicProfileView, NotificationListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',  UserLoginView.as_view(),    name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('upload/', PicUploadView.as_view(), name='upload_pic'),
    path('photos/<int:pk>/', PicDetailView.as_view(), name='pic_detail'),
    path('photos/<int:pk>/delete/', PicDeleteView.as_view(), name='pic_delete'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('search/', UserSearchView.as_view(), name='user_search'),
    path('user/<str:username>/', PublicProfileView.as_view(), name='user_public_profile'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),

]
