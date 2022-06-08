from pyexpat import model
from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

class Auth(models.Model):
    user_id=models.IntegerField()
    login=models.CharField(max_length=25)
    password=models.CharField(max_length=25) #?????

class Rating(models.Model):
    user_id=models.IntegerField()
    name=models.CharField(max_length=25)
    solved_number=models.IntegerField()
    total_grade=models.IntegerField() #????
    rating=models.IntegerField()

class Problem(models.Model):
    module_id=models.IntegerField()
    problem_id=models.IntegerField()
    description=models.CharField(max_length=1000)
    # input=models.Ta
    problem_code=models.BinaryField()