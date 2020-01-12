from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import CourseListView,CourseDetailView,LessonDetailView
app_name="courses"
urlpatterns = [
    path('',CourseListView.as_view(),name="list"),
    path('<slug>',CourseDetailView.as_view(),name="detail"),
    path('<course_slug>/<lesson_slug>',LessonDetailView.as_view(),name="lesson_detail"),
]