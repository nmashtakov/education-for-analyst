from rest_framework import generics
from django.shortcuts import render
from .models import Lesson, Block
from .serializers import EducationSerializer, BlockSerializer


# queryset - возвращает список записей клиенту
class EducationAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = EducationSerializer


class BlockAPIView(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class BlockAPICrud (generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer