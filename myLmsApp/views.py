from modulefinder import Module
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Grade, Profile, Problem, Chat, Module, ProblemIO

class baseView(ListView):
    model=Grade
    template_name='base.html'  

class userGradeListView(ListView):
    model = Grade
    template_name = 'user_grades.html'
    result_list = Grade.objects.all()

class profileView(ListView):
    model = Profile
    template_name = 'user_profile.html'
    result_list=Profile.objects.all()

class moduleListView(ListView):
    model = Module
    template_name = 'modules.html'
    result_list = Module.objects.all()    

class problemListView(ListView):
    model= Problem
    template_name= 'problems.html'   #??? kak sdelat; nomer
    result_list=Problem.objects.all()

class problemIOView(ListView):
    model= ProblemIO
    template_name= 'problem_io.html'   #??? kak sdelat; nomer
    result_list=ProblemIO.objects.all()

# def mmdv(request):
#     Gradedisplay=Grade.objects.all()
#     Chatdisplay=Chat.objects.all()
#     Profiledisplay=Profile.objects.all()
#     return render(request, "base.html", {"Grade":Gradedisplay, "Chat":Chatdisplay, "Profile":Profiledisplay})

# class mmdv(ListView):
#     model=Grade
#     template_name='home.html'   

