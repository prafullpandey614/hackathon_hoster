from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=40,blank=True,null=True)
    def __str__(self) -> str:
        return f"{self.user}"

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created :
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
    
class Hackathon(models.Model):
    HACKATHON_TYPES = (
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    )
    organizer = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='media/background_images/')
    hackathon_image = models.ImageField(upload_to='media/hackathon_images/')
    type_of_submission = models.CharField(max_length=10, choices=HACKATHON_TYPES)
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return self.title

class HackathonParticipant(models.Model):
    participant = models.ForeignKey(Profile,on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon,on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to="media/submissions")
    def __str__(self) -> str:
        return f"{self.hackathon}  {self.participant}"
