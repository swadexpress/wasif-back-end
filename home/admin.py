import admin_thumbnails
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *

admin.site.register(Product)
