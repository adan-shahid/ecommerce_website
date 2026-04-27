from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import customUser

class customUserAdmin(UserAdmin):
    model = customUser

    
admin.site.register(customUser, customUserAdmin)