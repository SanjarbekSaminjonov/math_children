from django.shortcuts import render
from django.http import HttpResponse
from .models import SecondTask
from dashboard.models import AllResult
from random import shuffle

# Create your views here.

all_tasks = list()


def shuffle_answers(obj):
    answers = [
        obj.answer_true,
        obj.answer_1,
        obj.answer_2,
        obj.answer_3
    ]
    shuffle(answers)
    answers_with_ABCD = {
        'A': answers[0],
        'B': answers[1],
        'C': answers[2],
        'D': answers[3]
    }
    return answers_with_ABCD


def get_objects_second():
    question_objects = SecondTask.objects.all()
    question_objects_list = list(question_objects)
    shuffle(question_objects_list)

    four_obj = question_objects_list[:4]

    context = {
        'questions': {
            'question1': {
                'question': four_obj[0].question,
                'answers': shuffle_answers(four_obj[0])
            },
            'question2': {
                'question': four_obj[1].question,
                'answers': shuffle_answers(four_obj[1])
            },
            'question3': {
                'question': four_obj[2].question,
                'answers': shuffle_answers(four_obj[2])
            },
            'question4': {
                'question': four_obj[3].question,
                'answers': shuffle_answers(four_obj[3])
            },
        },
        'true_answers': {
            'true_answer1': four_obj[0].answer_true,
            'true_answer2': four_obj[1].answer_true,
            'true_answer3': four_obj[2].answer_true,
            'true_answer4': four_obj[3].answer_true,
        }
    }

    global all_tasks
    all_tasks = context


get_objects_second()


def second_task(request):
    context = {
        'questions': all_tasks['questions']
    }
    return render(request, 'second_app/second_task.html', context)


def check(request):
    true_answers = list(all_tasks['true_answers'].values())

    if request.method == 'POST':

        given_answers = list()
        given_answers.append(str(request.POST['question1']))
        given_answers.append(str(request.POST['question2']))
        given_answers.append(str(request.POST['question3']))
        given_answers.append(str(request.POST['question4']))

        check_results = list()

        count = 0
        for i in range(4):
            if given_answers[i] == true_answers[i]:
                count += 1
                check_results.append(True)
            else:
                check_results.append(False)

        result, created = AllResult.objects.get_or_create(
            pupil=request.user, type_task=2)

        result.last_score = count * 25
        result.add_attempt()
        result.save()

        my_result = list()

        for i in range(4):
            my_result.append({
                'my_answer': given_answers[i],
                'true_false': check_results[i]
            })

        context = {
            'results': my_result
        }

        return render(request, 'second_app/result.html', context)
