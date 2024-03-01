from django.contrib import admin
from django.contrib.auth.models import User,Group
# Register your models here.
from apps.base import models

# class SettingsFilterAdmin(admin.ModelAdmin):
#     list_filter = ('title', )
#     list_display = ('title', 'descriptions')
#     search_fields = ('title', 'descriptions')

class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')



admin.site.register(models.Slide, SlideFilterAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)