from django.db import models

# Create your models here.

class Channel(models.Model):
    Name = models.CharField(max_length=255,blank=False)
    Description = models.TextField(blank=True,default='')
    Friday = models.BooleanField(default=False)
    Saturday = models.BooleanField(default=False)
    Sunday = models.BooleanField(default=True)
    Monday = models.BooleanField(default=True)
    Tuesday = models.BooleanField(default=True)
    Wednesday = models.BooleanField(default=True)
    Thursday = models.BooleanField(default=True)
    standup_time = models.TimeField()
    standup_duration_minutes = models.IntegerField()

class Membership(models.Model):
    channel = models.IntegerField()
    user = models.TextField()
    view = models.BooleanField()
    report = models.BooleanField()
    manage = models.BooleanField()





