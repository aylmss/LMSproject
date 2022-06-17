from pyexpat import model
from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

class Grade(models.Model):
    user_id=models.ForeignKey('auth.user', on_delete=models.CASCADE)
    group_id=models.ForeignKey('auth.group', on_delete=models.CASCADE)
    problem_id=models.ForeignKey('myLmsApp.problem', on_delete=models.CASCADE)
    problem_grade=models.IntegerField() 
    # class Meta:
    #     db_table="table1"

class Module(models.Model):
    module_id=models.IntegerField()
    title=models.CharField(max_length=100)
    m_description=models.CharField(max_length=1000)

class Problem(models.Model):
    problem_id=models.IntegerField()
    module_id=models.ForeignKey('myLmsApp.module', on_delete=models.CASCADE)
    description=models.CharField(max_length=1000)

class ProblemIO(models.Model):
    problem_id=models.ForeignKey('myLmsApp.problem', on_delete=models.CASCADE)
    input=models.CharField(max_length=1000)
    output=models.CharField(max_length=1000) 

class Chat(models.Model):
    user_id=models.ForeignKey('auth.user', on_delete=models.CASCADE)
    message=models.CharField(max_length=1000)
    date=models.DateField()
    class Meta:
        db_table="table2"

class Profile(models.Model):
    user_id=models.ForeignKey('auth.user', on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    photo=models.ImageField(upload_to ='uploads/')
    github=models.URLField(max_length = 200)