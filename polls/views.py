from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.


def index(request):
    """
    question_list = Question.objects.all()
    output = ",".join([question.question_text for question in question_list])
    return HttpResponse(output)
    """
    question_list = Question.objects.all()
    template = loader.get_template("polls/index.html")
    context = {
        "question_list" : question_list,
    }
    return HttpResponse(template.render(context,request))

def details(request, question_id):
    return HttpResponse(f"Youre looking at Question {question_id}")

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response, {question_id})

def vote(request, question_id):
    response = f"You're voting on question {question_id}."
    return HttpResponse(response)
