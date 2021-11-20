from time import timezone
from django.contrib.auth.models import User
from django.db import models

# Это наш manager model
class PublishedManager(models.Manager):
    def get_published_posts(self):
        return super().get_published_posts().filter(status='published')

class Post(models.Model):
    # ...
    objects = models.Manager()
    published = PublishedManager()
    # ...
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    choices = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    status = models.CharField(max_length=10, choices=choices, default='true')

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title
