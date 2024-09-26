from django.db import models
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                               related_name='tasks_author')
    executor = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                                 null=True, blank=True,
                                 related_name='tasks_executor')
    labels = models.ForeignKey(Label, on_delete=models.PROTECT, null=True,
                               blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
