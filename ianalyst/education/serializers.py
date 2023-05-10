from rest_framework import serializers
from .models import Lesson, Block


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'block', 'lesson_name')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"
