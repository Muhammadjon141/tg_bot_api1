import requests
from django.views import View, generic
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserRegisterForm, UserLoginForm

class Get_info_api:
    @staticmethod
    def get_token_login(username, password):
        url = 'http://localhost:8001/auth/login'
        data = {
            "username_or_email": username,
            "password": password
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            token = response.json()["token"]["access_token"]
            return token
        else:
            return 'failed'
           
    @staticmethod
    def get_token_register(username, email, password):
        url = 'http://localhost:8001/auth/register'
        data = {
            "username": username,
            "email": email,
            "password": password
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()["token"]["access_token"]
        else:
            return 'failed'    

    
class Index_View(View):
    def get(self, request, *args, **kwargs):
        size = int(request.GET.get('size', 4))
        page = int(request.GET.get('page', 1))
        url = f'http://localhost:8001/comment/comments/?size={size}&page={page}'
        response = requests.post(url)
        if response.status_code == 200:
            return render(request, 'index.html', context={"comments":response})
        else:
            return render(request, 'index.html', context={"comments":response})
        

class Login_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            token = Get_info_api.get_token_login(username, password)
            request.session['auth_token'] = token
            return redirect('home') 
        else:
            return render(request, 'login.html', {'form': form})
    
class Register_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            url = 'http://localhost:8001/auth/register'
            data = {
                "username": username,
                "email": email,
                "password": password
            }
            response = requests.post(url, json=data)
            if response.status_code == 200:
                return HttpResponse("User registered successfully!")
            else:
                return HttpResponse(f"Error: {response.json()['detail']}")
        else:
            form = UserRegisterForm()
            return render(request, 'register.html', {'form': form})