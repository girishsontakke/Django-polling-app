from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .models import Question, Choice
from .forms import QuestionCreationForm


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        messages.warning(request, "You haven't selected any choice")
        return render(request, 'polls/detail.html', {
            'question': question,
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def questionCreation(request):
    if request.method == "POST":
        form = QuestionCreationForm(request.POST)
        if form.is_valid() and request.user.is_staff:
            form.save()
            return redirect("polls:index")
        else:
            return redirect("polls:index")

    else:
        form = QuestionCreationForm()

    return render(request, "polls/question_form.html", {"form": form})
