from rest_framework import serializers
from django.contrib.auth.models import User

from api import models


class QuestionSerializers(serializers.ModelSerializer):

    class Meta:
        model=models.Questions
        fields="__all__"

class AnswerSerializers(serializers.ModelSerializer):

    class Meta:
        model=models.Answers
        fields="__all__"        


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','groups']