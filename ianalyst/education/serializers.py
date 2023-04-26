from rest_framework import serializers
from .models import Lesson

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('block', 'lesson_name')
