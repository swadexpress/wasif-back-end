from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'auth_provider', 'created_at']


admin.site.register(User, UserAdmin)
admin.site.register(OTPToken)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email' ]
    list_filter = ['custom_id','user']
    search_fields = ['custom_id','user']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileImages)
