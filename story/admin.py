from django.contrib import admin
from .models import Story
from django.contrib.auth.models import Group

# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url']


admin.site.unregister(Group)
admin.site.register(Story, StoryAdmin)
