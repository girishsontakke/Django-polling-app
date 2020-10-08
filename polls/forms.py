from django import forms
from .models import Question, Choice


class QuestionCreationForm(forms.Form):
    question_text = forms.CharField(max_length=100)
    choice1 = forms.CharField()
    choice2 = forms.CharField()
