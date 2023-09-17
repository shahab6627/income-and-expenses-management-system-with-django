from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IncomeSource(models.Model):
    source = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.source
    
class UserIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income_from = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=False)
    income_source = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self) -> str:
        return f'{self.user} got {self.amount} from {self.income_source}'
    