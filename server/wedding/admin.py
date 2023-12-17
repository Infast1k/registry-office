from django.contrib import admin
from .models import Wedding, WeddingStatus, Witnesses

admin.site.register(WeddingStatus)
admin.site.register(Wedding)
admin.site.register(Witnesses)
