from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Post(models.Model):
    post_category = {
        ('RELATIONSHIP', 'Relationship'),
        ('LIFE', 'Life Coaching'),
        ('LEADERSHIP', 'Leadership'),
        ('ENTREPRENEURSHIP', 'Entrepreneurship')
    }

    user_post = models.ForeignKey(User, on_delete=models.CASCADE, auto_created=True, default=1)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=64, verbose_name="Post Category", choices=post_category, default='LIFE')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
