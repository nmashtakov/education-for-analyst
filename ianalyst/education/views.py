from rest_framework import generics

from .models import Lesson, Block
from .permissions import IsAdminOrReadOnly
from .serializers import LessonSerializer, BlockSerializer


# queryset - возвращает список записей клиенту
class LessonAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonAPICrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAdminOrReadOnly,)


class BlockAPIView(generics.ListAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class BlockAPICrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = (IsAdminOrReadOnly,)


