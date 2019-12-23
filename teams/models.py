from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=255,blank=False)
    description = models.TextField(blank=True,default='')

class Role(models.Model):
    team_id = models.IntegerField()
    role_name = models.CharField(max_length=255)
    member_email = models.CharField(max_length=255)

class Invitation(models.Model):
    team_id = models.IntegerField()
    role_name = models.CharField(max_length=255)
    member_email = models.CharField(max_length=255)


