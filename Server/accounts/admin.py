from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    ordering = ('uid',)
    list_display = ('uid', 'name', 'role', 'department_id', 'is_active')

    fieldsets = (
        (None, {'fields': ('uid', 'password')}),
        ('Personal Info', {'fields': ('name', 'role', 'department_id')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('uid', 'name', 'role', 'department_id', 'password1', 'password2'),
        }),
    )

    search_fields = ('uid', 'name')
    list_filter = ('role', 'department_id')
