from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserModel(UserAdmin):
    list_display=['username','email','role']
admin.site.register(CustomUser,UserModel)
