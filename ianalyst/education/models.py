from django.db import models
from django.contrib.auth.models import AbstractUser

from education.auth import UserProfileManager


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=256, blank=False)
    content = models.TextField(blank=True)
    block = models.ForeignKey('Block', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.lesson_name


class Block(models.Model):
    block_name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.block_name


class Test(models.Model):
    test_name = models.CharField(max_length=256, blank=False)
    block = models.ForeignKey('Block', on_delete=models.CASCADE, null=False)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.test_name


class QuestionAnswer(models.Model):
    question = models.CharField(max_length=256, blank=False)
    answer = models.CharField(max_length=256, blank=False)
    is_correct = models.BooleanField(default=False)
    block = models.ForeignKey('Block', on_delete=models.PROTECT, null=False)
    lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT, null=False)
    test = models.ForeignKey('Test', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.question, self.answer


class TestResult(models.Model):
    user_answer = models.CharField(max_length=256, blank=False)
    block = models.ForeignKey('Block', on_delete=models.PROTECT, null=False)
    lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT, null=False)
    test = models.ForeignKey('Test', on_delete=models.PROTECT, null=False)
    question = models.ForeignKey('QuestionAnswer', on_delete=models.PROTECT, null=False)
    user = models.ForeignKey('User', on_delete=models.PROTECT, null=False)


class PassedLesson(models.Model):
    block = models.ForeignKey('Block', on_delete=models.PROTECT, null=False)
    lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT, null=False)
    user = models.ForeignKey('User', on_delete=models.PROTECT, null=False)


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)

    objects = UserProfileManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
