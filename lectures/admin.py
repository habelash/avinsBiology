from django.contrib import admin
from .models import LectureVideos
# Register your models here.

admin.site.site_header = "Anin's Biology"


class VideosDisplay(admin.ModelAdmin):
    list_display = ('topic', 'link')
    list_display_links = ('topic', 'link')


admin.site.register(LectureVideos, VideosDisplay)
