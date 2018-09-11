from django.urls import path
from my_project import views
from .views import IndexView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('my_univer/', views.first_html_page, name="first_html_page"),
    path('add_student/', views.AddStudent.as_view(), name="add_student"),
    path('add_teacher/', views.AddTeacher.as_view(), name="add_teacher"),
]