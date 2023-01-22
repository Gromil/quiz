from django.db import models


class Choice(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class MultipleChoice(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=255)
    choices = models.ManyToManyField(Choice, blank=True)
    multiple_choices = models.ManyToManyField(MultipleChoice, blank=True)

    def __str__(self) -> str:
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, blank=True)
    multiple_choices = models.ManyToManyField(MultipleChoice, blank=True)


class Questionnaire(models.Model):
    name = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)

    def __str__(self) -> str:
        return self.name


class Result(models.Model):
    request = models.CharField(max_length=10)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer)
