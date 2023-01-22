from rest_framework import serializers

from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import (
    Result, Answer, Choice, MultipleChoice, Question, Questionnaire
)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer


class ResultSerializer(WritableNestedModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Result


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Choice


class MultipleChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MultipleChoice


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    multiple_choices = MultipleChoiceSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Question


class QuestionnaireSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Questionnaire
