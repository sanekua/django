from django.urls import path
from my_project import views

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.index, name="index"),
    path('add_student/', views.add_student, name="add_student"),

]