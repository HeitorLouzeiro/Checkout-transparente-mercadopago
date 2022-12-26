import mercadopago
from django.conf import settings

from django.shortcuts import render

sdk = mercadopago.SDK(settings.ACCESS_TOKEN)

# Create your views here.


def home(request):
    card_data = {
        "card_number": "5031433215406351",
        "security_code": "123",
        "expiration_month": "12",
        "expiration_year": "2025",
        "cardholder": {
            "name": "Heitor Louzeiro",
            "identification": {
                "type": "CPF",
                "number": "12345678909"
            }
        }
    }
    card_token_response = sdk.card_token().create(card_data)
    card_token = card_token_response["response"]["id"]
    print(card_token)

    payment_data = {
        "transaction_amount": 100,
        "token": card_token,
        "description": "Teste de pagamento",
        "installments": 1,
        "payer": {
            "email": "heitorlouzeiro2019@gmail.com",

        }
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    print(payment)
    return render(request, 'payments/pages/home.html')
