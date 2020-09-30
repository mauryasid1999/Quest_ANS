from django.db import models

# Create your models here.
class Questions(models.Model):

    title=models.TextField()


    def __str__(self):
        return self.title


class Answers(models.Model):

    Solutions=models.TextField()

    def __str__(self):
        return self.Solutions

    