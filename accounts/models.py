from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='post_images/', default='post_images/default_profile_pic.jpg')
    def __str__(self):
        return self.user.username
