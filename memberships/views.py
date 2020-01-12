from django.shortcuts import render
from .models import Course,Lesson
# Create your views here.
from django.views.generic import ListView,DetailView

class CourseListView(ListView):
    model = Course
class CourseDetailView(DetailView):
    model = Course