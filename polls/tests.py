from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime

# Create your tests here.


class PollTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        question_text = "Test Question"
        question = Question(question_text=question_text, pub_date=timezone.now() +
                            datetime.timedelta(days=30))
        self.assertIs(question.was_published_recently(), False)


class PollTestAnother(TestCase):
    def test_str_method_of_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        question_text = "Test1 Question"
        question = Question(question_text=question_text)
        self.assertIs(self._question(question), question_text)

    def _question(self, question):
        return question.__str__()
