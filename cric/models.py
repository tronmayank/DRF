from pyexpat import model
from django.db import models
from matplotlib.pyplot import title


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    createdAt = models.DateTimeField(auto_now=True, null= True)
    updatedAt = models.DateTimeField(auto_now=False, null=True)
    def __str__(self):
        return self.name

class Tags(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now=True, null= True)
    updatedAt = models.DateTimeField(auto_now=False, null=True)
    def __str__(self):
        return self.title

class songs(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    sungby = models.ForeignKey(singer, on_delete=models.CASCADE, related_name='singer')
    tags = models.ManyToManyField(Tags, blank=True, related_name='songs')

    createdAt = models.DateTimeField(auto_now=True, null= True)
    updatedAt = models.DateTimeField(auto_now=False, null=True)
    def __str__(self):
        return self.title



class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    song = models.ForeignKey(songs, on_delete=models.CASCADE, related_name='comments')
    createdAt = models.DateTimeField(auto_now=True, null= True)
    updatedAt = models.DateTimeField(auto_now=False, null=True)