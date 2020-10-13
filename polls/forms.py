from django import forms
from django.forms import widgets
from .models import Question, Choice


class QuestionCreationForm(forms.Form):
    question_text = forms.CharField(max_length=100, widget=widgets.TextInput(
        attrs={'placeholder': 'Enter your question'}))
    choice1 = forms.CharField()
    choice2 = forms.CharField()
