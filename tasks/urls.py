from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [

    path('auth/register', RegisterView.as_view()),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/me', MeView.as_view()),

    path('tasks', TaskListCreateView.as_view()),
    path('tasks/<int:pk>', TaskDetailView.as_view()),
]