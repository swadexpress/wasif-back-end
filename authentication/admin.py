from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'auth_provider', 'created_at']


admin.site.register(User, UserAdmin)
admin.site.register(OTPToken)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email' ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileImages)
