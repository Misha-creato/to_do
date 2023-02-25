from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(
        verbose_name='title',
        max_length=100
    )

    # def __str__(self) -> str:
    #     return self.title


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
        verbose_name='author',
        to=User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    created_at = models.DateTimeField(
        verbose_name='created_at',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='updated_at',
        auto_now=True,
    )
    is_done = models.BooleanField(
        verbose_name='is_done',
        default=False
    )
    category = models.ForeignKey(
        verbose_name='category',
        to='Category',
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    def __str__(self) -> str:
        return self.title
