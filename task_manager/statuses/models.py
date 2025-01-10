from django.db import models


class Statuses(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
