from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignupForm

# Create your views here.


def login_user(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Username yoki parol noto'g'ri!"
    else:
        form = LoginForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def signup_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)
