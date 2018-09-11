import datetime

from django.utils import timezone
from django.db import models
import re
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, RegexValidator,ValidationError


class Person(models.Model):
    firname = RegexValidator(regex=r'^[a-zA-Z]+\s?[a-zA-Z]+\s?[a-zA-Z]+$')
    first_name = models.CharField(validators=[firname], max_length=30, blank=True)
    laname = RegexValidator(regex=r'^[a-zA-Z]+[-]?[a-zA-Z]+$')
    last_name = models.CharField(validators=[laname], max_length=30, blank=True)
    email = models.EmailField(null=True)
    phone_regex = RegexValidator(regex=r'^\+\d{9,13}$',
                                 message="Phone number must be \
                                 entered in the format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        abstract = True


class Answer(models.Model):
    text = models.CharField(max_length=50)



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Quiz(models.Model):
    title = models.CharField(max_length=255, default="Name this quiz plz")
    questions = models.ManyToManyField(Question, related_name="questions")

    def __str__(self):
        return "{}".format(self.title)


class Student(Person):
    avg_mark = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    quizzes = models.ManyToManyField(Quiz)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Teacher(Person):
    subject = models.CharField(max_length=50)
    quizzes = models.ForeignKey(Quiz, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)



class Class(models.Model):
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    title = models.CharField(max_length=100)

    def __str__(self):
        return "{}...".format(self.title[:12])