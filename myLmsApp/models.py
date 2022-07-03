from pyexpat import model
from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

class Grade(models.Model):
    user_id=models.ForeignKey('auth.user', on_delete=models.CASCADE)
    group_id=models.ForeignKey('auth.group', on_delete=models.CASCADE)
    module_id=models.ForeignKey('myLmsApp.module', on_delete=models.CASCADE)
    problem_id=models.ForeignKey('myLmsApp.problem', on_delete=models.CASCADE)
    problem_title=models.ForeignKey('myLmsApp.problemio', on_delete=models.CASCADE)
    problem_grade=models.IntegerField()
    # class Meta:
    #     db_table="table1"

    def __str__(self):
        return str(self.user_id)+' '+str(self.problem_title)

class Module(models.Model):
    module_id=models.IntegerField()
    title=models.CharField(max_length=100)
    m_description=models.TextField()

    def __str__(self):
        return self.title

class Problem(models.Model):
    problem_id=models.IntegerField()
    module_id=models.ForeignKey('myLmsApp.module', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.problem_id)

class ProblemIO(models.Model):
    problem_id=models.ForeignKey('myLmsApp.problem', on_delete=models.CASCADE)
    problem_title=models.CharField(max_length=100)
    description=models.TextField()
    input=models.TextField()
    output=models.TextField()

    def __str__(self):
        return str(self.problem_id)+' '+str(self.problem_title)
     

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

    def __str__(self):
        return self.username

