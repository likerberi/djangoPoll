from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls.index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
        # return super().get_queryset() default constructed return
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # default contructed
    # model = ModelName
    # template_name=''
    
class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# changed by code_GENERIC
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     #(2)template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)
#     #(2)return HttpResponse(template.render(context, request))
    
#     #(1)output = ', '.join([q.question_text for q in latest_question_list])
#     #(1)return HttpResponse(output)

# def detail(request, quesion_id):
#     question = get_object_or_404(Question, pk=quesion_id)
#     return render(request, 'polls/detail.html', {'question': quesion})
#     #                       template, context, content_type
#     # return HttpResponse("You're looking at question %s" % quesion_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # response = "You are looking at results of question %s"
#     # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1;
        selected_choice.save()
        #Always return an HttpResponseRedirect after successfully dealing
        #with POST data. This prevents data from being posted twice if a 
        #user hits the Back button.
        return HttpResponseRedirect(reverse('polls/results', args=(question.id,)))


    return HttpResponse("You are voting on question %s" % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    