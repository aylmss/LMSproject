from django.urls import path
from .views import gradeListView, baseView, mmdv

urlpatterns=[  
    # path('', gradeListView.as_view(), name='home'),
    path('', baseView.as_view(), name='base'),
    path('home', mmdv.as_view(), name='home'),
    path('grades', gradeListView.as_view(), name='grades'),
]