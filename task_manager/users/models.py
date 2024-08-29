from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


class Users(models.Model):
    title = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    published = PublishedManager()
