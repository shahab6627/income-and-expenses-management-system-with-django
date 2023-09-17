from django.core.mail import send_mail 
from django.conf import settings 

from django.urls import reverse
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str 
from django.contrib.auth.tokens import PasswordResetTokenGenerator

def sendActivationMail(email, subject,message):
    # link = f'http://localhost:8000/authentication/activate-account/{token}-{uid}'
    # subject = "Expanses management system account activation mail"
    # message = f'click on given link to activate your account \n {link}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    
    send_mail(subject, message, from_email, recipient_list)
    
    return "mail send "