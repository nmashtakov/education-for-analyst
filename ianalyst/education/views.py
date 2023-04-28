from rest_framework import generics
from django.shortcuts import render
from .models import Lesson
from .serializers import EducationSerializer


# Create your views here.
class EducationAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = EducationSerializer
