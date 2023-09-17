from django.shortcuts import render, redirect
from django.views import View
from .models import UserIncome, IncomeSource
from settings_app.models import UserCurrencyType
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

class UserIncomeView(View):
    
    def get(self, request, username):
        user_currency_type = UserCurrencyType.objects.filter(user = request.user).exists()
        if user_currency_type:
            user_currency = UserCurrencyType.objects.get(user = request.user)
        else:
            user_currency = "None"
        income_sources = IncomeSource.objects.all()
        user_incomes = UserIncome.objects.filter(user = request.user)
        total_income = 0
        if user_incomes:
            for income in user_incomes:
                total_income += income.amount
        context = {
            'incomes':user_incomes,
            'total_income':total_income,
            'user_currency':user_currency,
            'income_sources':income_sources
        }
        return render(request, 'income/index.html', context)
        
        
    def post(self, request, username):
        
        income = request.POST['income']
        amount = request.POST['amount']
        source = request.POST['income_source']
        description = request.POST['description']
        date = request.POST['date']
        income_id = request.POST['income_id']
        
        if income_id == "":
            UserIncome.objects.create(
                user = request.user,
                income_from = income,
                amount = amount,
                income_source = source,
                description = description,
                date = date
            )
            
            
            messages.add_message(request, messages.SUCCESS, 'income added')
            return redirect('income', username=request.user)
        else:
            get_user_income = UserIncome.objects.get(id = income_id)
            
            get_user_income.income_from = income
            get_user_income.amount = amount 
            get_user_income.income_source = source 
            get_user_income.description = description 
            if date == "":
                get_user_income.save()
            else:
                get_user_income.date = date 
                get_user_income.save()
            
            messages.add_message(request, messages.SUCCESS, 'income updated')
            return redirect('income', username=request.user)
            


    