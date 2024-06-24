from django.db import models


# Create your models here.
class Users(models.Model):
    title = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
