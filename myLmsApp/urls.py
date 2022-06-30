from django.urls import path
from .views import  profileView, moduleListView, baseView,problemListView, problemIOView, userGradeListView

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
    path('problem_io_detail/<int:pk>/', problemIOView.as_view(), name='problem_io_detail'),
    path('chat', views.chat_index, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
    #path('home', mmdv.as_view(), name='home'),
]