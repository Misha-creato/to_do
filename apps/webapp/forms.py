from django.forms import ModelForm
from .models import Task, Category

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'category'
        ]


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
        ]