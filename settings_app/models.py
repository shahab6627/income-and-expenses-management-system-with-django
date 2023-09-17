from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserCurrencyType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency_type = models.CharField(max_length=100, default="USD", blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.user} - currency type is {self.currency_type}'