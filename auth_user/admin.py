from django.contrib import admin
from .models import User, UserResult


@admin.register(User)
class UserAdminAdmin(admin.ModelAdmin):
    list_display = ["email", "email_verify", 'cat', 'bis_type']
    list_filter = ['email']


@admin.register(UserResult)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'answer']
    list_filter = ['user']
    search_fields = ['user__email']
