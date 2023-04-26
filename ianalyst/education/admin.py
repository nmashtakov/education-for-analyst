from django.contrib import admin

from .models import Lesson
from .models import Block

admin.site.register(Lesson)
admin.site.register(Block)

