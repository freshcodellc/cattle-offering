from django.contrib import admin

from .models import Cattle, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class CattleAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]

admin.site.register(Cattle, CattleAdmin)
