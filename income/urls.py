from django.urls import path 
from .views import *

urlpatterns = [
    path('<str:username>', UserIncomeView.as_view(), name='income')
]