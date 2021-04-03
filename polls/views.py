from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout

from .models import Question, Choice, User
from .forms import LoginForm, QuestionCreationForm
from .decorators import no_user_required


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")


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
        selected_choice.votes.add(request.user)
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


@no_user_required
def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username", "")
            password = form.cleaned_data.get("password", "")
            user = get_object_or_404(User, username=username)
            if check_password(password, user.password):
                login(request, user)
                messages.success(
                    request, f"successfully login {user.username}")
                return redirect("polls:index")
            messages.warning(request, "please check your credentials")
            return render(request, 'registration/login.html', {"form": form})
        messages.warning(request, "please check your credentials")
        return render(request, 'registration/login.html', {"form": form})
    form = LoginForm()
    return render(request, 'registration/login.html', {"form": form})


def logoutView(request):
    logout(request)
    return redirect("login")
