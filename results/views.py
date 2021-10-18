from django.db.models.expressions import F
from django.shortcuts import render
from dashboard.models import AllResult
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.


def results_dashboard(request):
    return render(request, 'results/results_dashboard.html')


def results_table(request):

    allFirstTaskResults = AllResult.objects.filter(type_task=1)
    allSecondTaskResults = AllResult.objects.filter(type_task=2)
    allThirdTaskResults = AllResult.objects.filter(type_task=3)


def search_pupil_result(request):

    searchResult = AllResult.objects.filter(pupil__first_name__contains="Oy").filter(type_task=2)

    print(searchResult)
    return HttpResponse("1")
    # if request.method == 'GET':
    #     search_results = list(AllResult.objects.values())
    #     return JsonResponse(search_results, safe=False)
