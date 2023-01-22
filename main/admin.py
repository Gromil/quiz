from django.contrib import admin

from .models import (
    Answer, Choice, MultipleChoice, Question, Questionnaire, Result
)

admin.site.register(Answer)
admin.site.register(Choice)
admin.site.register(MultipleChoice)
admin.site.register(Question)
admin.site.register(Questionnaire)
admin.site.register(Result)
