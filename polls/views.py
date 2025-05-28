from django.shortcuts import get_object_or_404,render
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # دوباره فرم رأی رو نشون بده و یه پیام خطا اضافه کن
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "لطفاً یه گزینه انتخاب کن!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # بعد از ذخیره رأی، ریدایرکت کن به صفحه نتایج
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})