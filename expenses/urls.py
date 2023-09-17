from django.urls import path 
from .views import * 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('<str:username>', login_required(UserExpensesView.as_view() ,login_url='/login'), name='home'),
    path('delete-expense/<str:id>',DeleteExpenseView.as_view(), name="deleteExpense"),
    path('search-expense/<str:search_val>',csrf_exempt(searchExpenseView.as_view()), name="searchExpense"),
    path('expenses-summary/<str:username>', getExpenseSummary, name="expenses-summary"),
    path('expenses-summary/display-chart/display', expenseSummaryChart, name="expense-chart")
]
