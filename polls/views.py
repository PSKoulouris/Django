from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.db.models import F
from django.urls import reverse

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

"""
def detail(request, question_id):
    return HttpResponse(f"Youre looking at Question {question_id}")
"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/results.html", {"question": question})

"""
def vote(request, question_id):
    response = f"You're voting on question {question_id}."
    return HttpResponse(response)
"""

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message": "You did not select a choice",
            },
        )
    else: 
        selected_choice.vote = F('vote') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        

