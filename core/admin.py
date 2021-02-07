from django.contrib import admin

from core.models import RegisterPermission

@admin.register(RegisterPermission)
class RegisterPermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
