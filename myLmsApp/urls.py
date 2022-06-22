from django.urls import path
from .views import userGradeListView, baseView, profileView, moduleListView, problemListView, problemIOView

from . import views

urlpatterns=[  
    # path('', gradeListView.as_view(), name='home'),
    path('', baseView.as_view(), name='base'),
    path('user_grades', userGradeListView.as_view(), name='user_grades'),
    path('user_profile', profileView.as_view(), name='user_profile'),
    path('modules', moduleListView.as_view(), name='modules'),
    path('problems', problemListView.as_view(), name='problems'),
    path('problem_io', views.index, name='problem_io'),
    path('runcode', views.runcode, name='runcode'),
    path('test', problemIOView.as_view(), name='test'),
    #path('home', mmdv.as_view(), name='home'),
]