import json
from payment.api.models import AddressInfoApiModel
from user.models import UserProfile
from django.shortcuts import render
from requests import api
from django.shortcuts import get_object_or_404
from pprint import pprint
import iyzipay
from django.shortcuts import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from config.settings.base import PAYMENT_OPTIONS
from payment.api.serializers import ProductSerializer
from products.models import BasketModel
from payment.models import PaymentModel
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.models import User


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')


class Payment(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request, *args, **kwargs):
        # request_host = request.get_host()
        # path = reverse('api:payment:result')
        # callback_url = f'{request_host}{path}'

        user_profile: UserProfile = get_object_or_404(UserProfile, user=request.user)
        user: User = get_object_or_404(User, id=request.user.id)
        callback_url = f'{request.scheme}://{request.get_host()}{reverse('api:payment:result')}'
        payment_model: PaymentModel = PaymentModel.objects.create()
        basket_model: BasketModel = BasketModel.objects.first()
        print(basket_model.get_products())
        basket_items = ProductSerializer(basket_model.get_products(), many=True).data
        pprint(basket_items[0])
        print(basket_model.get_total_price())
        buyer = {
            'id': 'BY789',
            'name': 'John',
            'surname': 'Doe',
            'gsmNumber': '+905350000000',
            'email': 'email@email.com',
            'identityNumber': '74300864791',
            'lastLoginDate': '2015-10-05 12:43:35',
            'registrationDate': '2013-04-21 15:12:09',
            'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
            'ip': get_client_ip(request),
            'city': 'Istanbul',
            'country': 'Turkey',
            'zipCode': '34732'
        }

        address = AddressInfoApiModel.load(user_profile)
        address = address.get_dict()

        card = {
            'cardHolderName': "Faruk",
            'cardNumber': "5890040000000016",
            'expireYear': "26",
            'expireMonth': "4",
            'cvc': "123",
            'registerCard': "0",
            'cardAlias': "",
            'cardToken': "",
            'cardUserKey': "",
        }

        request: dict = {
            'locale': 'tr',
            'conversationId': payment_model.conversationId,
            'price': basket_model.get_total_price(),
            'paidPrice': basket_model.get_total_price(),
            'currency': 'TRY',
            'basketId': 'B67832',
            'paymentGroup': 'PRODUCT',
            "callbackUrl": callback_url,
            "enabledInstallments": ['2', '3', '6', '9'],
            'buyer': buyer,
            'shippingAddress': address,
            'billingAddress': address,
            'basketItems': basket_items,
        }
        request["paymentCard"] = card
        request["buyerEmail"] = user.email

        checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(request, PAYMENT_OPTIONS)

        basic = iyzipay.BasicPayment().create(request, PAYMENT_OPTIONS)

        print("BASIC PAY")

        pprint(basic)
        basic_read = basic.read().decode('utf-8')
        pprint(json.loads(basic_read))







        print("BASIC PAY - END")

        # print(checkout_form_initialize.read().decode('utf-8'))
        page = checkout_form_initialize
        header = {'Content-Type': 'application/json'}
        content = checkout_form_initialize.read().decode('utf-8')
        print(content)
        json_content = json.loads(content)
        print(json_content)
        pprint(json_content)
        payment_model.token = json_content["token"]
        payment_model.save()
        print(type(json_content))
        print(json_content["checkoutFormContent"])
        print("************************")
        print(json_content["token"])
        print("************************")
        form = json_content["checkoutFormContent"]
        # form.replace('<script>', '')
        # form.replace('</script>', '')
        return Response({'message': 'ok :)', 'context': json_content["checkoutFormContent"]}, status=201)


