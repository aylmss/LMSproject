from django.urls import path
from .views import  profileView, moduleListView, baseView,problemListView, problemIOView, userGradeListView, problemIOUpdateView

from . import views

urlpatterns=[  
    # path('home', gradeListView.as_view(), name='home'),
    path('', baseView.as_view(), name='base'),
    path('user_grades', userGradeListView.as_view(), name='user_grades'),
    path('user_profile', profileView.as_view(), name='user_profile'),
    path('modules', moduleListView.as_view(), name='modules'),
    path('problems', problemListView.as_view(), name='problems'),
    path('runcode', views.runcode, name='runcode'),
    path('problem_detail/<int:pk>/', problemIOView.as_view(), name='problem_detail'),
    path('problem_detail/<int:pk>/update/', problemIOUpdateView.as_view(), name='problem_update'),
    path('chat', views.chat_index, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('base2', views.mmdv, name='base2'),
]