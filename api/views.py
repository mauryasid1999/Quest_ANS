from rest_framework.response import Response
from api import models,serializers
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin



from rest_framework.generics import(

ListCreateAPIView,


)


class questionlistview(ListCreateAPIView):
    queryset=models.Questions.objects.all()
    serializer_class=serializers.QuestionSerializers
    permissions_classes=[permissions.IsAuthenticated]
    group_required = [u'Moderator']
    



class answerlistview(ListCreateAPIView):
    queryset=models.Answers.objects.all()
    serializer_class=serializers.AnswerSerializers
    permissions_classes=[permissions.IsAuthenticated]
    group_required = [u'Users']
    

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializers
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]

