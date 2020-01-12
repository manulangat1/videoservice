from django.urls import path
from .views import getAccessToken
app_name='mpesa'
urlpatterns = [
    path('access/token',getAccessToken,name="get_mpesa_access_token")
]