from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.TextField(
        verbose_name='title', 
        max_length=200,
        help_text='task title'
    )
    description = models.TextField(
        verbose_name='description',
        max_length=400,
        help_text='task description'
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    def __str__(self) -> str:
        return self.title