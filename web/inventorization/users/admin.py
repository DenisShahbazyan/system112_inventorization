from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'first_name', 'last_name',
                    'is_staff')
    list_editable = ('username', 'email', 'role', 'first_name', 'last_name',
                     'is_staff')
    search_fields = ('username', 'email', 'role', 'is_staff')
    list_filter = ('email', 'role', 'username')
