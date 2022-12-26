import json
import os

import mercadopago
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

sdk = mercadopago.SDK(settings.ACCESS_TOKEN)

# Create your views here.


def home(request):
    template_name = 'payments/pages/home.html'
    context = {
        'public_key': os.environ.get('PUBLIC_KEY'),
    }
    return render(request, template_name, context)


@csrf_exempt
def processpayment(request):
    data_json = request.body
    data = json.loads(data_json)
    payment_data = {
        "transaction_amount": float(data["transaction_amount"]),
        "token": data["token"],
        "installments": int(data["installments"]),
        "payment_method_id": data["payment_method_id"],
        "issuer_id": data["issuer_id"],
        "payer": {
            "email": data["payer"]["email"],
            "identification": {
                "type": data["payer"]["identification"]["type"],
                "number": data["payer"]["identification"]["number"]
            }
        }
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    print("status =>", payment["status"])
    print("status_detail =>", payment["status_detail"])
    print("id =>", payment["id"])
    return render(request, 'payments/pages/home.html')
