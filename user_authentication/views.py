from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
import json 
from django.contrib.auth.models import User
from django.http import JsonResponse
from validate_email import validate_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode 
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.contrib import messages

# Create your views here.
from .utils import sendActivationMail

class UserRegistrationView(View):
        
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home',username=request.user)
        return render(request, 'user_authentication/register.html')
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        password = data['password']
        
        user = User.objects.create_user(username = username, email=email, password=password)
        user.is_active = False
        user.save()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        link = f'http://localhost:8000/authentication/activate-account/{token}-{uid}'
        subject = "Expanses management system account activation mail"
        message = f'click on given link to activate your account \n {link}'
        sendActivationMail(email, subject,message)
        return JsonResponse({'success':'a verification email is send to the '+ email+' please activate your account'})

class ActivateAccountView(View):
    def get(self, request, token, uid):
        print(token)
        print(uid)
        user_id = urlsafe_base64_decode(force_str(uid))
        print(user_id)
        try:
            user = User.objects.get(id = user_id)
            if user.is_active:
                print('user already active')
                messages.add_message(request, messages.SUCCESS, 'your account is already in active state')
                return redirect('login')

            if not PasswordResetTokenGenerator().check_token(user, token):
                context = {
                    'heading':"we can't activate your account",
                    'message':'activation link not working, it may be changed...'
                }                
                return render(request, 'user_authentication/tokenproblem.html', context)
            user.is_active = True
            user.save()
            print('user is now activated')
            messages.add_message(request, messages.SUCCESS, 'your account is activated. you can login now.')
            return redirect('login')
        
        except Exception as e:
            print(e)
        return redirect('login')
    
class ValidateUsernameView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
    
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username only contain alphanumeric'}, status=400)
        if len(username) < 4:
            return JsonResponse({'username_error':'to short username!'})
        if User.objects.filter(username = username).exists():
            return JsonResponse({'username_error':'username already taken'})
            
        return JsonResponse({'success':'available'}, status=200)

class ValidateEmailView(View):
    def post(self, request):
        data = json.loads(request.body)
        user_email = data['user_email']
        print(user_email)
        if not validate_email(user_email):
            return JsonResponse({'email_error':'invalid email'})
        
        
        if User.objects.filter(email=user_email).exists():
            return JsonResponse({'email_error':'email already exists'})
        return JsonResponse({'success':'good to go'})
        
            
            

class UserLoginView(View):
    
    def get(self, request):            
        return render(request, 'user_authentication/login.html')
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
  
        # user = User.objects.filter(username = username, password=password).exists()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success':True,'username':username})
            
        return JsonResponse({'login_error':'username or password incorrect'})


class ChangePasswordView(View):
    def get(self, request):
        return render(request, 'user_authentication/change-password.html')

class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'user_authentication/reset-password.html')


def user_logout(request):
    
    logout(request)
    return redirect('login')

class ResetPasswordSendMailView(View):
    def get(self, request):
        return render(request, 'user_authentication/reset-password.html')
    
    def post(self, request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            email = request.POST['email']
            
            try:
                getEmail = User.objects.get(email=email)
                token = PasswordResetTokenGenerator().make_token(getEmail)
                uid = urlsafe_base64_encode(force_bytes(getEmail.pk))
                link = f'http://localhost:8000/reset-password/{token}-{uid}'
                subject = 'reset your Expense Account Password'
                message = f'click on below link to reset your passwod \n {link}'
                email_response = sendActivationMail(email, subject,message)
                return JsonResponse({'msg':email_response})
            except Exception as e:
                print(e)
                return JsonResponse({'error':"email not exists"})
                
                
class ResetUserPasswordView(View):
    def get(self, request, token, uid):
        user_id = urlsafe_base64_decode(force_str(uid))
        print(user_id)
        user = User.objects.get(id = user_id)
        check_token = PasswordResetTokenGenerator().check_token(user, token)
        if not check_token:
            context = {
                    'heading':"password reset problem.!",
                    'message':'password reset link is not working it may be changed or token is expired..!'
                }  
            return render(request, 'user_authentication/tokenproblem.html', context)
        
        return render(request, 'user_authentication/reset-password-form.html')
    
    def post(self, request, token,uid):
        password = request.POST['password']
        r_password = request.POST['r_password']
        if password != r_password:
            context = {
                'password':password,
                'r_password': r_password
            }
            messages.add_message(request, messages.SUCCESS, 'passwords are not matching')
            return render(request, 'user_authentication/reset-password-form.html', context)
        
        else:
            user_id = urlsafe_base64_decode(force_str(uid))
            try:
                user = User.objects.get(id = user_id)
                check_token = PasswordResetTokenGenerator().check_token(user, token)
                if check_token:
                    user.set_password(password)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'password reset successfully. try with your new password')
                    return redirect('login')
            except Exception as e:
                messages.add_message(request, messages.SUCCESS, 'reset password token is not valid')
                return render(request, 'user_authentication/reset-password-form.html')