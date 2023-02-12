from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

# Create your views here.
def index_view(request):
    if request.user.is_authenticated:
    
        tasks = Task.objects.filter(author=request.user.id)

        context = {'tasks': tasks}
        return render(
            request=request,
            template_name='index.html',
            context=context
        )
    else:
        return redirect('accounts:login')


def create_view(request,):
    if request.user.is_authenticated:

        form = TaskForm()
        context = {'form': form}
        if request.method == 'POST':
            form = TaskForm(data=request.POST)
            if form.is_valid():
                Task.objects.create(**form.cleaned_data, author=request.user)
                return redirect('index')
        return render(
            request=request,
            template_name='create.html',
            context=context
        )
    else:
        return redirect('accounts:login')


def detail_view(request, pk):
    if request.user.is_authenticated:

        task = get_object_or_404(Task, pk=pk)
        context = {'task': task}
        return render(
            request=request, 
            template_name='detail.html', 
            context=context
        )
    else:
        return redirect('accounts:login')


def update_view(request, pk):
    if request.user.is_authenticated:

        task = get_object_or_404(Task, pk=pk)
        print(task)
        form = TaskForm(instance=task)

        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                for key, value in form.cleaned_data.items():
                    setattr(task, key, value)
                task.save()
        context = {'form': form}
        return render(
            request=request,
            template_name='update.html',
            context=context
        )
    else:
        return redirect('accounts:login')


def delete_view(request, pk):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'POST':
            task.delete()
            return redirect('index')
        else:
            context = {'task': task}
            return render(
                request=request,
                template_name='delete.html',
                context=context
            )
    else:
        return redirect('accounts:login')


