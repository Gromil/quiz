from django.contrib import admin
from django.urls import path

from rest_framework import routers

from main.views import ResultViewSet, QuestionnaireViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.SimpleRouter()

router.register('results', ResultViewSet)
router.register('questionnaires', QuestionnaireViewSet)

urlpatterns += router.urls
