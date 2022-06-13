from django.db import router
from django.urls import path,include
# from rest_framework import routers
from . import views



urlpatterns = [
    # path('students', views.Student_Data_View  , name="studentdata"),
    path('students', views.Student_Create  , name="studentdata"),
    path('student/<int:pk>', views.Student_Data_Update  , name="studentupdate"),
  
]