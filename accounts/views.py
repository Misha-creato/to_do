from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        print(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Created account for user ' + username)
            return redirect('login')
        else:   
            messages.error(request, form.errors)

    context = {'form': form}
    return render(
        request=request, 
        template_name='register.html', 
        context=context
    )


def login_view(request):
    context = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request=request, 
            username=username, 
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(
        request=request,
        template_name='login.html',
        context=context
    )


def logout_view(request):
    logout(request=request)
    return redirect('login')




