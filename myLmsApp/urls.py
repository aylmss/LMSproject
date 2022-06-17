from django.urls import path
#from .views import gradeListView
from .views import baseView
from . import views

urlpatterns=[  
    # path('', gradeListView.as_view(), name='home'),
    path('', baseView.as_view(), name='base'),
    path('home', views.mmdv.as_view(), name='home'),
]