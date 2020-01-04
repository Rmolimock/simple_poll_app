from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def answers(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/answers.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/answers.html', {
            'question': question,
            'error_message': 'Please select a choice.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def draft(request):
    return render(request, 'polls/draft.html')

def create_question(request):
    from django.utils import timezone
    q_text = request.POST['question_text']
    q = Question(pub_date=timezone.now(), question_text=q_text)
    q.save()
    if len(request.POST['choice_text_a']) > 0:
        choice = Choice(question=q, votes=0, choice_text=request.POST['choice_text_a'])
        choice.save()
    if len(request.POST['choice_text_b']) > 0:
        choice = Choice(question=q, votes=0, choice_text=request.POST['choice_text_b'])
        choice.save()
    for c_num in range(len(request.POST) - 4):
        if len(request.POST['choice_text' + str(c_num)]) > 0:
            choice = Choice(question=q, votes=0, choice_text=request.POST['choice_text' + str(c_num)])
            choice.save()

    return index(request)

def add_answer(request):
        return HttpResponseRedirect(reverse('polls:index'))
