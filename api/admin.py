from django.contrib import admin

from api.models import Hackathon, HackathonParticipant,Profile, Submission


admin.site.register(Hackathon)
admin.site.register(Profile)
admin.site.register(HackathonParticipant)
admin.site.register(Submission)
