"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('my_project/',include('my_project.urls')),
# ]


from django.urls import path,include
from django.contrib import admin
from my_project import views

from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('admin/', admin.site.urls),
    path('univer/',include('my_project.urls')),
    path('', include('my_project.urls')),
    path('', include('django.contrib.auth.urls')),
    # path('my_univer/', views.first_html_page, name="first_html_page"),
    # path('add_student/', views.add_student, name="add_student"),
    # path('add_teacher/', views.add_teacher, name="add_teacher")
]


