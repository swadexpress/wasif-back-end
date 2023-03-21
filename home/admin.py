from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *
import admin_thumbnails

admin.site.register(BannerImages)
admin.site.register(P2PMessageUniqueId)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(PostImages)
admin.site.register(Images)

