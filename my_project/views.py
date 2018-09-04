from django.shortcuts import render

# Create your views here.

# from django.http import JsonResponse
#
# from .models import Student
#
# def index(request):
#     s = Student.objects.create(
#         first_name="Jonnf", last_name='Tsdfjsdf',email='jonh@gmsil.com'
#     )
#     print(s)
#     print(24)
#     return JsonResponse({'msg':'University apps'})


from django.shortcuts import render


def index(request):
    return render(request, "index.html")



from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import StudentForm


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid(): # валидация формы
            #print(form.data[“first_name”])
            return JsonResponse({"message": "Form was processed"})
        data = {'form': form} # вернет форму с введенной информацией
    else:
        data = {'form': StudentForm()} # новая форма

        #return data
        return render(request, 'my_project/add_student.html', data)
