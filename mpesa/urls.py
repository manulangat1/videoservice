from django.urls import path
from . import views
from .views import getAccessToken,lipa_na_mpesa_online
app_name='mpesa'
urlpatterns = [
    path('access/token',getAccessToken,name="get_mpesa_access_token"),
    path('lipa_na_mpesa',lipa_na_mpesa_online,name="lipa_na_mpesa"),
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),

]