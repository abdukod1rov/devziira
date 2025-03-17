from django.db import models
from devziira.apps.accounts.models import CustomUser

class Post(models.Model):
    title = models.CharField(verbose_name='Title of the post', max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    sub_room = models.ForeignKey('SubRoom', on_delete=models.CASCADE)
    likes = models.IntegerField(default=1)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255, blank=True)
    liked_by = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=155, unique=True)
    description = models.TextField()


    def __str__(self):
        return self.name


class SubRoom(models.Model):
    name = models.CharField(max_length=155, unique=True)
    owner = models.ForeignKey(CustomUser, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(CustomUser, related_name='liked_comments', blank=True)
