import mercadopago
from django.conf import settings

from django.shortcuts import render

sdk = mercadopago.SDK(settings.ACCESS_TOKEN)

# Create your views here.


def home(request):
    return render(request, 'payments/pages/home.html')
