from django.db import models
from django.contrib.auth.models import User

# Extended information about a user, if required.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    # Any other fields specific to the user's profile

# A collection of flashcards on a specific topic or subtopic.
class Deck(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Individual flashcards with a question (front) and an answer (back).
class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # For spaced repetition algorithm
    next_review_date = models.DateTimeField()
    interval = models.PositiveIntegerField(default=1)
    ease_factor = models.FloatField(default=2.5)
    repetitions = models.PositiveIntegerField(default=0)

# Represents a study or quiz session.
class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    # You can add fields to store results, e.g., number of cards reviewed, accuracy, etc.

# Represents questions generated using OpenAI API for simulated exams.
class GeneratedQuestion(models.Model):
    QUESTION_TYPES = (
        ('MCQ', 'Multiple Choice Question'),
        ('ESSAY', 'Essay'),
        ('FIB', 'Fill in the Blanks')
    )

    type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    content = models.TextField()  # The question content
    answer = models.TextField()   # The generated answer
    study_session = models.ForeignKey(StudySession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
