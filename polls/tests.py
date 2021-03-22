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
