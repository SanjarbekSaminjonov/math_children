from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from first_app.views import get_questions
from second_app.views import get_objects_second
from third_app.views import get_questions_third

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'dashboard/home.html')


@login_required(login_url='home')
def dashboard(request):
    get_questions()
    get_objects_second()
    get_questions_third()
    return render(request, 'dashboard/dashboard.html')
