from django.db.models.expressions import F
from django.shortcuts import render
from dashboard.models import AllResult
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.


def results_dashboard(request):
    return render(request, 'results/results_dashboard.html')


def results_table(request, type_task):

    taskResults = AllResult.objects.filter(
        type_task=type_task).order_by('-avarage_score')
    my_result, created = AllResult.objects.get_or_create(
        pupil=request.user, type_task=type_task)

    text = request.GET.get('searching_text')

    if text != None:
        taskResults = taskResults.filter(pupil__first_name__contains=text)

    context = {
        'task_results': taskResults,
        'my_result': my_result,
    }

    return render(request, 'results/index.html', context)


def search_pupil_result(request):

    searchResult = AllResult.objects.filter(
        pupil__first_name__contains="Oy").filter(type_task=2)

    print(searchResult)
    return HttpResponse("1")
    # if request.method == 'GET':
    #     search_results = list(AllResult.objects.values())
    #     return JsonResponse(search_results, safe=False)
