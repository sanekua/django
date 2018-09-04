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