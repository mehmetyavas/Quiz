from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from src.api.serializers import *
from src.models import *

# class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionDetailSerializer


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionDetailSerializer


class AnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerDetailSerializer
