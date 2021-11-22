from django.contrib.auth.models import User
from django.db import models

# Это наш manager model
from django.urls import reverse
from django.utils.timezone import now


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    # ...
    objects = models.Manager()
    published = PublishedManager()
    # ...
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    choices = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    status = models.CharField(max_length=10, choices=choices, default='published')

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def statya_urli(self):
        return reverse('tuit:post_detail', args=[self.publish.year,
                                                 self.publish.month, self.publish.day, self.slug])

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments", verbose_name='пост')
    name = models.CharField(max_length=250)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    text = models.TextField(verbose_name="Текст Коммента")
    time_cr = models.DateTimeField(auto_now_add=True, verbose_name="Время создание коммент")
    time_up = models.DateTimeField(default=now)

    class Meta:
        ordering = ('-time_cr', )

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


