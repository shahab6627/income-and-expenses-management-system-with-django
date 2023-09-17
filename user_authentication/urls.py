from django.urls import path 
from .views import * 
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(UserRegistrationView.as_view()), name="register"),
    path('login', csrf_exempt(UserLoginView.as_view()), name="login"),
    path('change-password', ChangePasswordView.as_view(), name="change-password"),
    path('rest-password', ResetPasswordView.as_view(), name='reset-password'),
    path('validate-username', csrf_exempt(ValidateUsernameView.as_view()), name="validate_username"),
    path('validate-email', csrf_exempt(ValidateEmailView.as_view()), name="validate_email"),
    path('activate-account/<token>-<uid>', ActivateAccountView.as_view(), name="activate-account"),
    path('logout', user_logout, name="user_logout"),
    path('reset-password-send-mail', ResetPasswordSendMailView.as_view(), name="resetpassword"),
    path('reset-password/<token>-<uid>', csrf_exempt(ResetUserPasswordView.as_view()), name="reset-password")
]
