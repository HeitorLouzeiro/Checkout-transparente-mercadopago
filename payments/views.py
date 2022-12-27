import json
import os

import mercadopago
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

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
            "installments": 1,
            "payment_method_id": data["payment_method_id"],
            "payer": {
                "email": data["payer"]["email"],
                "identification": {
                    "type": "CPF",
                    "number": "191191191-00",
                }
            }
        }

        payment_response = sdk.payment().create(payment_data)
        payment = payment_response["response"]

        print("status =>", payment["status"])
        print("status_detail =>", payment["status_detail"])
        print("id =>", payment["id"])
        response = redirect('/pending/')
        return response


def resultpayment(request):
    template_name = 'payments/pages/resultpayments.html'
    context = {
        'public_key': os.environ.get('PUBLIC_KEY'),
    }
    return render(request, template_name, context)
