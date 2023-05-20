from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


from education.views import *

urlpatterns = [
    path('api_schema/', get_schema_view(
            title='ИС "Я хочу стать аналитиком"',
            description='Документация разработчика Swagger'
            ), name='api_schema'),
    path('docs/', TemplateView.as_view(
            template_name='docs.html',
            extra_context={'schema_url':'api_schema'}
            ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path(r"auth/token/", TokenObtainPairView.as_view()),
    path(r"auth/token/refresh/", TokenRefreshView.as_view()),
    path('api/', include('education.urls', namespace='education')),
    path('signup', SignUpAPICrud.as_view()),
    path('api/v1/block/', BlockAPIView.as_view()),  # просмотр блоков
    path('api/v1/block/<int:pk>/', BlockAPICrud.as_view()),  # изменение/удаление блоков
    path('api/v1/block/lessons/', LessonAPIView.as_view()),  # просмотр уроков
    path('api/v1/block/lessons/<int:pk>', LessonAPICrud.as_view()),  # изменение/удаление уроков
]
