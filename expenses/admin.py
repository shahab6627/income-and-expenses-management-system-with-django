from django.contrib import admin
from .models import ExpenseCategory, UserExpense
# Register your models here.
admin.site.register(UserExpense)
admin.site.register(ExpenseCategory)
