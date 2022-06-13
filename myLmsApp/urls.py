from django.urls import path
#from .views import gradeListView
from . import views

urlpatterns=[  
    # path('', gradeListView.as_view(), name='home'),
    path('', views.mmdv, name='home')
]