from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Pic, Comment, Like, Follower, CustomUser, Notification


@admin.register(Pic)
class PicAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_filter  = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'pic', 'user', 'created_at')
    list_filter  = ('created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'pic', 'user', 'created_at')
    list_filter  = ('created_at',)

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'followed', 'created_at')
    list_filter  = ('created_at',)

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_pic')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
admin.site.register(Notification)