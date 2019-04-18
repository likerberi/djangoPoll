from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #(2)template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    #(2)return HttpResponse(template.render(context, request))
    
    #(1)output = ', '.join([q.question_text for q in latest_question_list])
    #(1)return HttpResponse(output)

def detail(request, quesion_id):
    question = get_object_or_404(Question, pk=quesion_id)
    return render(request, 'polls/detail.html', {'question': quesion})
    #                       template, context, content_type
    # return HttpResponse("You're looking at question %s" % quesion_id)

def results(request, question_id):
    response = "You are looking at results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)