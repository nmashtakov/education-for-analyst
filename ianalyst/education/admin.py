from django.contrib import admin
from .models import Lesson, Test, Block, QuestionAnswer, TestResult, PassedLesson, User


admin.site.register(Lesson)
admin.site.register(Block)
admin.site.register(Test)
admin.site.register(QuestionAnswer)
admin.site.register(TestResult)
admin.site.register(PassedLesson)
admin.site.register(User)
