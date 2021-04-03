from django import forms
from django.forms import widgets
from .models import Question, Choice, User


class QuestionCreationForm(forms.Form):
    question_text = forms.CharField(max_length=100, widget=widgets.TextInput(
        attrs={'placeholder': 'Enter your question'}))
    choice1 = forms.CharField(max_length=255)
    choice2 = forms.CharField(max_length=255)

    def save(self):
        validated_data = self.cleaned_data
        self.create(validated_data)

    def create(self, validated_data):
        question_text = validated_data.get('question_text', "")
        choice1 = validated_data.get('choice1', "")
        choice2 = validated_data.get('choice2', "")

        question = Question.objects.create(question_text=question_text)
        Choice.objects.create(question=question, choice_text=choice1)
        Choice.objects.create(question=question, choice_text=choice2)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=widgets.TextInput(
        attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(max_length=100, widget=widgets.PasswordInput(
        attrs={'placeholder': 'Enter your username'}))
