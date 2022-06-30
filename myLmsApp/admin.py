from django.contrib import admin
from .models import  Chat, Module, Profile, Grade, Problem, ProblemIO
# Register your models here.
admin.site.register(Grade)
admin.site.register(Chat)
admin.site.register(Module)
admin.site.register(Problem)
admin.site.register(ProblemIO)
admin.site.register(Profile)