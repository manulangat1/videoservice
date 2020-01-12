from django.contrib import admin

# Register your models here.
from .models import MpesaCallBacks,MpesaCalls,MpesaPayment

admin.site.register(MpesaCallBacks)
admin.site.register(MpesaCalls)
admin.site.register(MpesaPayment)