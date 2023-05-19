from rest_framework import generics

from .models import Lesson, Block, User
from .permissions import IsAdminOrReadOnly
from .serializers import LessonSerializer, BlockSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid


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


class SignUpAPICrud(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignUpAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
