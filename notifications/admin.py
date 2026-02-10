from django.contrib import admin
from .models import Notification

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'message', 'created_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('user__email', 'message')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'