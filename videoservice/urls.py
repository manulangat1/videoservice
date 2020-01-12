
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('memberships/',include('memberships.urls',namespace="memberships")),
    path('admin/', admin.site.urls),
    path('',include('courses.urls',namespace="courses")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)