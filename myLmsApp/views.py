from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Grade, Profile, Problem, Chat
class gradeListView(ListView):
    model = Grade
    template_name = 'grades.html'
    result_list = Grade.objects.all()



# class profileView(ListView):
#     model = Profile
#     template_name = 'home.html'

# class problemView(ListView):
#     model= Problem
#     template_name= 'problem.html'   #??? kak sdelat; nomer

# def mmdv(request):
#     Gradedisplay=Grade.objects.all()
#     Chatdisplay=Chat.objects.all()
#     return render(request, "home.html", {"Grade":Gradedisplay, "Chat":Chatdisplay})

class mmdv(ListView):
    model=Grade
    template_name='home.html'   

class baseView(ListView):
    model=Grade
    template_name='base.html'  