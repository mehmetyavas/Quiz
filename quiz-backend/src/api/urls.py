from django.urls import path
from src.api import views as api_views

urlpatterns = [
    path('questions/', api_views.QuestionListCreateAPIView.as_view(), name='questions'),
    path('questions/<int:pk>/', api_views.QuestionDetailAPIView.as_view(), name='question-detail'),
    path('answers/', api_views.AnswerListCreateAPIView.as_view(), name='answers'),
    path('answers/<int:pk>', api_views.AnswerDetailAPIView.as_view(), name='answer-detail'),
]
