from django.contrib import admin
from .models import Grade, Chat, Module, Problem, ProblemIO, Profile
# Register your models here.
admin.site.register(Grade)
admin.site.register(Chat)
admin.site.register(Module)
admin.site.register(Problem)
admin.site.register(ProblemIO)
admin.site.register(Profile)