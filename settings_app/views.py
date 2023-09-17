from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import os 
import json
from .models import UserCurrencyType
from  django.contrib import messages
# Create your views here.

class CurrencyChangeView(View):
    def get(self, request):
        user_currency = UserCurrencyType.objects.filter(user = request.user).exists()
        if user_currency:
            current_user_currency = UserCurrencyType.objects.get(user = request.user)
        else:
            current_user_currency = ""
        currencyList = []
        file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
        with open(file_path, 'r') as currencyFile:
            filedata = json.load(currencyFile)
            for key,value in filedata.items():
                currencyList.append({'name':key, 'value':value})     

        context = {
            'currency_list':currencyList,
            'selected_currency': current_user_currency
        }
        # import pdb; pdb.set_trace()
        return render(request, 'settings_app/currency_setting.html', context)
    def post(self, request):
        user = request.user
        currency = request.POST['currency']
        user_currency = UserCurrencyType.objects.filter(user = request.user).exists()
        if user_currency:
            current_user_currency = UserCurrencyType.objects.get(user = request.user)
            current_user_currency.currency_type = currency
            current_user_currency.save()
            messages.add_message(request, messages.SUCCESS, 'currency type updated')
            return redirect('change-currency')
            
        else:
            my_currency = UserCurrencyType.objects.create(user = user, currency_type = currency)
            my_currency.save()
            messages.add_message(request, messages.SUCCESS, 'currency updated')
            return redirect('change-currency')
        