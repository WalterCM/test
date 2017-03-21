#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Exam, Choice

def index(request):
    latest_exam_list = Exam.objects.order_by('-pub_date')[:5]
    for exam in latest_exam_list:
        print(exam.exam_name)
    context = {
        'latest_exam_list': latest_exam_list
    }

    return render(request, 'exams/index.html', context)

def detail(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'exams/detail.html', {'exam':exam})

def evaluate(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    selected_choices = {}

    response = "Selected choices: "
    for question in exam.question_set.all():
        try:
            selected_choice = question.choice_set.get(pk=request.POST['question' + str(question.id)])
        except (KeyError, Choice.DoesNotExist):
            choice_id = -1
        else:
            choice_id = selected_choice.id

        response += str(choice_id) + " "
        selected_choices[question.id] = choice_id
    #reversestr = reverse('exams:results', args=(exam_id,))
    #print("reverse " + reversestr)
    #return render(reversestr)

    return results(request, exam_id, selected_choices)

def results(request, exam_id, selected_choices):
    exam = get_object_or_404(Exam, pk=exam_id)
    correct_count = 0
    total_count = len(exam.question_set.all())
    for question in exam.question_set.all():
        choice_id = selected_choices[question.id]
        if choice_id is not -1 and Choice.objects.get(pk=choice_id).is_correct():
            correct_count += 1

    percentage = correct_count / total_count * 100
    return render(request, 'exams/results.html', {'percentage': percentage})