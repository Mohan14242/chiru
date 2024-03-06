from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class topic(models.Model):
    name=models.CharField(max_length=2000)
    def __str__(self):
        return self.name
class room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class message(models.Model):

    room=models.ForeignKey(room,on_delete=models.CASCADE)
    body=models.TextField(max_length=1000)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


