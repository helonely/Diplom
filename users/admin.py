from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'phone')
    list_filter = ('id', 'email', 'full_name', 'phone')
    search_fields = ('id', 'email', 'full_name', 'phone')
