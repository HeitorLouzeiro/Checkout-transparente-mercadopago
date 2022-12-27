import json
import os

import mercadopago
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

sdk = mercadopago.SDK(settings.ACCESS_TOKEN)

# Create your views here.


def home(request):
    if request.method == 'GET':
        template_name = 'payments/pages/home.html'
        context = {
            'public_key': os.environ.get('PUBLIC_KEY'),
        }
        return render(request, template_name, context)


def processpayment(request):
    if request.method == 'POST':
        data_json = request.body
        data = json.loads(data_json)
        payment_data = {
            "transaction_amount": float(data["transaction_amount"]),
            "description": "Título do produto",
            "payment_method_id": data["payment_method_id"],
            "payer": {
                "email": "test@test.com",
                "first_name": "Test",
                "last_name": "User",
                "identification": {
                    "type": "CPF",
                    "number": "191191191-00"
                },
                "address": {
                    "zip_code": "06233-200",
                    "street_name": "Av. das Nações Unidas",
                    "street_number": "3003",
                    "neighborhood": "Bonfim",
                    "city": "Osasco",
                    "federal_unit": "SP"
                }
            }
        }

        payment_response = sdk.payment().create(payment_data)
        payment = payment_response["response"]
        print(payment)
        return HttpResponse(payment)


def resultpayment(request):
    template_name = 'payments/pages/resultpayments.html'
    context = {
        'public_key': os.environ.get('PUBLIC_KEY'),
    }
    return render(request, template_name, context)
