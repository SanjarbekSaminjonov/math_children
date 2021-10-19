from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import ThirdTask
from dashboard.models import AllResult
from random import shuffle

# Create your views here.

question_objects_list = list()


def get_questions_third():
    global question_objects_list
    question_objects = ThirdTask.objects.all()
    question_objects_list = list(question_objects)
    shuffle(question_objects_list)


get_questions_third()


def third_task(request):

    context = {
        'question1': question_objects_list[0],
        'question2': question_objects_list[1],
        'question3': question_objects_list[2],
        'question4': question_objects_list[3],
    }

    return render(request, 'third_app/third_task.html', context)


def check(request):

    if request.method == 'POST':

        given_answers = [
            request.POST['answer_1'],
            request.POST['answer_2'],
            request.POST['answer_3'],
            request.POST['answer_4'],
        ]

        true_answers = [
            question_objects_list[0].question_answer,
            question_objects_list[1].question_answer,
            question_objects_list[2].question_answer,
            question_objects_list[3].question_answer,
        ]

        check_result = list()

        count = 0

        for i in range(4):
            if str(true_answers[i]) == str(given_answers[i]):
                count += 1
                check_result.append('To\'g\'ri')
            else:
                check_result.append('Noto\'g\'ri')

        result, created = AllResult.objects.get_or_create(
            pupil=request.user, type_task=3)

        result.last_score = count * 25
        result.add_attempt()
        result.save()

        context = {
            'given_answers': given_answers,
            'true_answers': true_answers,
            'check_result': check_result,
        }

        return HttpResponse(count)
    else:
        return redirect('third_task')
