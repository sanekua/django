from django.urls import path
from my_project import views

urlpatterns = [
    path('', views.index, name="index"),

]