from django.contrib import admin
from .models import CustomUser


# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined','is_staff','is_superuser','privaligies']
    list_editable = ['is_active','is_staff','is_superuser','privaligies']


admin.site.register(CustomUser, CustomUserAdmin)


