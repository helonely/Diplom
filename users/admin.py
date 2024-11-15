from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'phone')
    list_filter = ('email', 'full_name', 'phone')
    search_fields = ('email', 'full_name', 'phone')
