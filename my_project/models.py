
#
# from django.db import models
#
#
# class Student(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#
#     def __str__(self):
#         return f'S({self.first_name}, {self.last_name},{self.email})'
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Teacher(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#
#     def __str__(self):
#         return f'S({self.first_name}, {self.last_name},{self.email})'
#
#     def __repr__(self):
#         return self.__str__()

#here
import datetime

from django.utils import timezone
from django.db import models
import re
from django.core.validators import MaxValueValidator, RegexValidator,ValidationError


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    #phone_number = models.CharField(max_length=13)
    phone_regex = RegexValidator(regex=r'^\+\d{9,13}$',
                                 message="Phone number must be entered in the format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # def phone_validation(phone_number: str):
    #     match = re.match(r'^\+\d{9,12}$', self.phone_number)
    #     if not match:
    #         print('Hello')
    #         raise ValidationError('Enter correct number')
    #
    #     return match

    class Meta:
        abstract = True

class Student(Person):
    avg_mark = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    # def __str__(self):
    #     return "{} {}".format(self.first_name, self.last_name)


class Teacher(Person):
    subject = models.CharField(max_length=40)



class Class(models.Model):
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    title = models.CharField(max_length=100)



class Answer(models.Model):
    text = models.CharField(max_length=50)



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

