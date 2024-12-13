from django.db import models


class Statuses(models.Model):
    name = models.CharField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
