from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Student


class StudentsList(ListView):
    model = Student
    template_name = 'student_list.html'


class StudentDetails(DetailView):
    model = Student
    template_name = 'student_detail.html'