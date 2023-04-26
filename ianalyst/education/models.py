from django.db import models

class Lesson(models.Model):
    lesson_name = models.CharField()
    content = models.TextField(blank=True)
    block = models.ForeignKey('Block', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.lesson_name

class Block(models.Model):
    block_name = models.CharField(max_length=50)

    def __str__(self):
        return self.block_name
"""
class Account(models.Model):
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=32, blank=False)
    surname = models.CharField(max_length=32, blank=True)
    email = models.CharField(max_length=256)
    birthday = models.DateField(blank=True)

    def __str__(self):
        return self.login

class Passed_lesson(models.Model):
    lesson = models.ForeignKey('Education', on_delete=models.PROTECT, null=False)
    account = models.ForeignKey('Account', on_delete=models.PROTECT, null=False)

class Test(models.Model):
    test_name = models.CharField(blank=False)
    lesson = models.ForeignKey('Education', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.test_name

class Question_and_answer(models.Model):
    question =
    answer =
    is_correct =
    lesson =
    test =

    def __str__(self):
        return self.question

class
"""