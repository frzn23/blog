from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length = 20)
    views = models.IntegerField(default=0)
    content = models.TextField()
    slug = models.CharField(max_length= 200)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " by "+ self.author


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.TimeField(default=now)

    def __str__(self):
        return self.comment[0:13]+"  ... by"+ self.user.username

