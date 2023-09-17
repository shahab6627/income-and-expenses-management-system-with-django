from django.contrib import admin
from .models import IncomeSource, UserIncome
from django.contrib.admin import ModelAdmin

# Register your models here.
admin.site.register(IncomeSource)

class UserIncomeModel(ModelAdmin):
    list_display = ['id', 'user' ,'income_from', 'amount', 'income_source','description','date']
    
    

admin.site.register(UserIncome, UserIncomeModel)