from .views import *
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('change-currency', login_required(CurrencyChangeView.as_view(),login_url="/authentication/login"), name="change-currency")
]
