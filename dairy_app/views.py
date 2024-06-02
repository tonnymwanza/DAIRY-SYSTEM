from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages

from . models import Products
from django.views import View
# Create your views here.

class HomeView(View):

    def get(self, request):
        product_list = Products.objects.all()
        context= {
            'product_list': product_list
        }
        return render(request, 'index.html', context)    

class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')
    
class ServicesView(View):

    def get(self, request):
        return render(request, 'services.html')
    
class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')
    
class ProductView(View):

    def get(self, request):
        product_list = Products.objects.all()
        context = {
            'product_list': product_list
        }
        return render(request, 'product.html', context)

def user_register(request): # user registration
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'the username is in user. try another one')
                return redirect('user_register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'the email is in use. find another one')
                return redirect('user_register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                return redirect('user_login')
        else:
            messages.error(request, 'ensure the passwords are matching')
            return redirect('user_register')
    return render(request, 'register.html')

def user_login(request): # user login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('home')
        else:
            messages.error(request, 'invalid details provided. make sure the password or username is correct')
            return redirect('user_login')
    return render(request, 'login.html')
