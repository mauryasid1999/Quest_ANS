from django.urls import path
from django.contrib.auth.decorators import login_required

from api import views

urlpatterns=[
    path('questions/',(views.questionlistview.as_view())),
    
    path('answers/',views.answerlistview.as_view()),

    

    

]