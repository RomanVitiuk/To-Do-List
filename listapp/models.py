from django.contrib.auth.models import User

from django.db import models

from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=255)
    time_created = models.DateField(auto_now_add=True)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tasks List Table'
        ordering = ['-time_created', ]
