import sys

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

def index(request):
    return render(request, 'problem_io.html')

def runcode(request):
    
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(codeareadata)  #example =>   print("hello world")

            sys.stdout.close()

            sys.stdout = original_stdout  #reset the standard output to its original value

            # finally read output from file and save in output variable

            output = open('file.txt', 'r').read()

        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e


    #finally return and render index page and send codedata and output to show on page

    return render(request , 'problem_io.html', {"code":codeareadata , "output":output})

def chat_index(request):
    return render(request, 'chat.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

# def mmdv(request):
#     Gradedisplay=Grade.objects.all()
#     Chatdisplay=Chat.objects.all()
#     Profiledisplay=Profile.objects.all()
#     return render(request, "base.html", {"Grade":Gradedisplay, "Chat":Chatdisplay, "Profile":Profiledisplay})

# class mmdv(ListView):
#     model=Grade
#     template_name='home.html'   

