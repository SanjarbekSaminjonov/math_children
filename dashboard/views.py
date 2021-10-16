from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'dashboard/home.html')


@login_required(login_url='home')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
