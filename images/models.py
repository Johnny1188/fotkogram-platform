from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/')
    text = models.TextField()
    pub_date = models.DateTimeField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_likes = models.IntegerField(default=0)
    def __str__(self):
        return self.text[:50]+".."
    def short_text(self):
        return self.text[:80]+"..see more"

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.liker.id) + "---" + str(self.post.id)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.text[:50]+".."
