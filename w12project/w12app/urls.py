
from django.urls import path, include

from w12app import views

urlpatterns = [

    path('',views.demo,name='demo'),
]