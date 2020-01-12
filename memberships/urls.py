from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import MembershipSelectView,PaymentView
app_name="memberships"
urlpatterns = [
    path('',MembershipSelectView.as_view(),name="select"),
    path('payment',PaymentView,name="payment"),
    # path('<course_slug>/<lesson_slug>',LessonDetailView.as_view(),name="lesson_detail"),
]