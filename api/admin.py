from django.contrib import admin

from api.models import Hackathon

# Register your models here.
# class HackathonAdmin(admin.ModelAdmin):
#     list_display = ('title')
admin.site.register(Hackathon)
