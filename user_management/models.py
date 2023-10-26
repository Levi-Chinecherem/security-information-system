from django.contrib.auth.models import User
from django.db import models

class SecurityIncident(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    involved_parties = models.ManyToManyField(User)
    
    def __str__(self):
        return self.title

class SecurityGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name
