from django.contrib import admin
from health.models import Videos

@admin.register(Videos)

class AdminVideo(admin.ModelAdmin):

    list_display=['link', 'field', 'pic']
