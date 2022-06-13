from getapp import views
from django.urls import path

urlpatterns = [
    path('', views.index , name = "index"),
    path('addstudent', views.add_student , name = "addstudent"),
    path('editstudent', views.edit_student , name = "editstudent"),
    path('deletestudent', views.delete_student , name = "deletestudent")
]
