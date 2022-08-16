from rest_framework import serializers
from src.models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id', 'answer']


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Questions
        fields = '__all__'
