from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExpenseCategory(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.category_name

class UserExpense(models.Model):
    expense = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = ("user expenses")

    def __str__(self):
        return f'{self.expense} - by {self.user} with amount of {self.amount}'

