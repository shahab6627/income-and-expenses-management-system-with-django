from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse
from .models import UserExpense, ExpenseCategory
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
class UserExpensesView(View):
    def get(self, request, username):
        try:
            expense_cats = ExpenseCategory.objects.all()
            
            user = User.objects.get(username=username)
            user_exp = UserExpense.objects.filter(user = user.id)
            paginator = Paginator(user_exp, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            total_expense_amount = 0
            for amount in user_exp:
                total_expense_amount+=amount.amount
            
            
            context = {
                'expense_cats':expense_cats,
                'user_expenses':page_obj,
                'total_amount' : total_expense_amount
            }
            return render(request, 'expenses/index.html', context)
            
        except Exception as e:
            return render(request, 'expenses/bad-request-404.html')
            
    
    def post(self, request, username):
        expense = request.POST['expense']
        amount = request.POST['amount']
        description = request.POST['description']
        expense_cat = request.POST['expense_cat']
        date = request.POST['date']
        expense_id = request.POST['expense_id']
        
        if expense_id =="":
            add_expense = UserExpense.objects.create(
                expense = expense, amount = amount,
                description = description, user = request.user,
                expense_category_id = expense_cat, date=date
            )
            add_expense.save()
            messages.add_message(request, messages.SUCCESS, 'expense added')
            return redirect('home', username=request.user)
            
        else:
            get_expense = UserExpense.objects.get(id = expense_id)
            
            if get_expense:
                get_expense.expense = expense
                get_expense.amount = amount
                get_expense.description = description
                get_expense.expense_category_id = expense_cat
                if date !="":
                    get_expense.date = date
                
                get_expense.save()
                messages.add_message(request, messages.SUCCESS, 'expense updated')
                return redirect('home', username=request.user)
                
class DeleteExpenseView(View):
    def get(self,request, id):
        expense_id = id
        get_expense = UserExpense.objects.filter(id = expense_id).exists()
        if get_expense is not None:
            expense = UserExpense.objects.get(id = expense_id)
            expense_name = expense.expense
            expense.delete()
            return JsonResponse({'success':'expense delete', 'expense':expense_name})
        return JsonResponse({'error':'something went wrong'})
        
class searchExpenseView(View):
    def get(self, request, search_val):
        search_res = UserExpense.objects.filter(expense__istartswith = search_val, user = request.user).values() | UserExpense.objects.filter(date__istartswith=search_val, user=request.user).values() | UserExpense.objects.filter(amount__startswith=search_val, user=request.user).values()
         
        searchResult = list(search_res)
        print(search_res)
        return JsonResponse(searchResult, safe=False)

def getExpenseSummary(request, username):

    return render(request, 'expenses/expense-summary.html')



def expenseSummaryChart(request):
    expense_summary = UserExpense.objects.filter(user = request.user)
    cats = []
    cat_summary = {}
    
    for x in expense_summary:
        cats.append(x.expense_category)
    
    for cat in cats:
        cat_expense_summary = UserExpense.objects.filter(expense_category = cat, user = request.user)
        amount = 0
        for i in cat_expense_summary:
            amount+=i.amount
        cat_summary[cat.category_name] = amount
    print(cat_summary)
    
    return JsonResponse({'chartdata':cat_summary})
    
   
    
            
    