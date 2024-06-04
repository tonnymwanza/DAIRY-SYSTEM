from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . forms import ContactForm
from . models import Products
from . models import Contact
from django.views import View
from . models import AnimalSelection
from . forms import AnimalSelectionForm
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
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact = Contact.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                subject=  form.cleaned_data['subject'],
                message = form.cleaned_data['message']
            )
            form = ContactForm()
            messages.info(request, 'Thanks for contacting us. Well get  back to you soon.')
        else:
            messages.error(request, 'error sending information')
        context = {
            'form': form
        }
        return redirect('contact')
class ProductView(View):

    def get(self, request):
        product_list = Products.objects.all()
        context = {
            'product_list': product_list
        }
        return render(request, 'product.html', context)

def register(request): # user registration
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'the username is in user. try another one')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'the email is in use. find another one')
                return redirect('user_register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                return redirect('signin')
        else:
            messages.error(request, 'ensure the passwords are matching')
            return redirect('register')
    return render(request, 'register.html')

def signin(request): # user login
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
            return redirect('signin')
    return render(request, 'login.html')

@login_required(login_url='signin')
def selection(request):
    form = AnimalSelectionForm()
    if request.method == 'POST':
        form = AnimalSelectionForm(request.POST or None)
        if form.is_valid():
            animal_object = AnimalSelection.objects.create(
                animal_id = form.cleaned_data['animal_id'],
                breed = form.cleaned_data['breed'],
                animal_age = form.cleaned_data['animal_age'],
                gender = form.cleaned_data['gender'],
                health_condition = form.cleaned_data['health_condition']
            )
            form = AnimalSelectionForm()
            messages.success(request, 'Info sent successfully')
        else:
            messages.error(request, 'error sending information')
    context = {
        'form': form
    }
    return render(request, 'selection.html', context)

@login_required(login_url='signin')
def breeding(request):
    return render(request, 'breeding.html')

@login_required(login_url='signin')
def milking(request):
    return render(request, 'milking.html')