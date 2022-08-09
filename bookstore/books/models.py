from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    page_count = models.IntegerField(default=0)
    image_url = models.CharField(max_length=256, null=True)
    short_description = models.CharField(max_length=256, null=True)
    long_description = models.TextField(null=True)
    authors = models.ManyToManyField('Author')
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']


class Author(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

