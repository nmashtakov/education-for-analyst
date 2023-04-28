from rest_framework import serializers
from .models import Lesson

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'block', 'lesson_name')
