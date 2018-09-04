from django import forms
from django.core.validators import RegexValidator
from .models import Teacher, Student, Class
import re
from django.db import models

class StudentForm(forms.Form):
    first_name = forms.CharField(label="Student's first name", max_length=100)
    last_name = forms.CharField(label="Student's last name", max_length=100)
    email = forms.EmailField(label="Type in an email here")

    # phone_regex = RegexValidator(regex=r'^\+\d{9,13}$',
    #                              message="Phone number must be entered in the format: '+999999999'.")
    # phone_number = forms.CharField(label="Type in a phone number here", validators=[phone_regex])
