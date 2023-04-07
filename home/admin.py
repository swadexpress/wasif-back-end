from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *
import admin_thumbnails


class SentGiftsAdmin(admin.ModelAdmin):
    list_display = ['room_admin_user_profile',
                    'sent_user_user_profile',
                    'receive_user_profile',
                    'time',]
    readonly_fields = ('time',)


admin.site.register(HostAgents)
admin.site.register(BuyCoinFromAgents)
admin.site.register(SentGifts, SentGiftsAdmin)
admin.site.register(BannerImages)
admin.site.register(P2PMessageUniqueId)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(PostImages)
admin.site.register(Images)
