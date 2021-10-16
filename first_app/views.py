from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import FirstTask
from dashboard.models import AllResult
from random import shuffle

# Create your views here.

question_objects_list = list()


def get_questions():
    global question_objects_list
    question_objects = FirstTask.objects.all()
    question_objects_list = list(question_objects)
    shuffle(question_objects_list)


get_questions()


def first_task(request):
    context = {
        'question1': question_objects_list[0],
        'question2': question_objects_list[1],
        'question3': question_objects_list[2],
        'question4': question_objects_list[3],
        'question5': question_objects_list[4],
    }
    return render(request, 'first_app/first_task.html', context)


def check(request):

    if request.method == 'POST':
        given_answers = [
            request.POST['answer_1'],
            request.POST['answer_2'],
            request.POST['answer_3'],
            request.POST['answer_4'],
            request.POST['answer_5'],
        ]

        count = 0

        for i in range(5):
            print(question_objects_list[i].question_answer, given_answers[i])
            if str(question_objects_list[i].question_answer) == given_answers[i]:
                print(True)
                count += 1

        result, created = AllResult.objects.get_or_create(
            pupil=request.user, type_task=1)

        result.last_score = count * 20
        result.add_attempt()
        result.save()

        return HttpResponse(count)
    else:
        return redirect('first_task')
