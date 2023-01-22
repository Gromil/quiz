from rest_framework import viewsets

from .serializers import ResultSerializer, QuestionnaireSerializer
from .models import Result, Questionnaire


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
