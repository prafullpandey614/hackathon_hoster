from django.contrib import admin

from api.models import Hackathon, HackathonParticipant,Profile

# Register your models here.
# class HackathonAdmin(admin.ModelAdmin):
#     list_display = ('title')
admin.site.register(Hackathon)
admin.site.register(Profile)
admin.site.register(HackathonParticipant)
