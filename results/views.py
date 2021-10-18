from django.shortcuts import render
from dashboard.models import AllResult

# Create your views here.


def results_dashboard(request):
    return render(request, 'results/results_dashboard.html')


def results_table(request, type_task):

    title = {
        1: "Nostandart topshiriq",
        2: "Mantiqiy savollar",
        3: "Kreativ fikrlash",
    }

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
        'title': title[type_task]
    }

    return render(request, 'results/index.html', context)
