from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, CategoryForm
from .models import Task, Category

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
        categories = Category.objects.all()
        context = {
            'form': form, 
            'categories': categories, 
        }
        if request.method == 'POST':
            # category = request.POST.get('category')
            # category_ins = Category.objects.get(title=category)
            form = TaskForm(data=request.POST)
            for field in form:
                print(field.name, field.errors)
            print(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
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
        form = TaskForm(instance=task)
        categories = Category.objects.all()

        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                for key, value in form.cleaned_data.items():
                    setattr(task, key, value)
                task.save()
                return redirect('index')
        context = {
            'form': form,
            'categories': categories
        }
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


def category_create_view(request):
    form = CategoryForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('index')
    return render(
        request=request,
        template_name='category_create.html',
        context=context
    )


    