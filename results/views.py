from django.shortcuts import render

# Create your views here.

def results_dashboard(request):
    return render(request, 'results/results_dashboard.html')