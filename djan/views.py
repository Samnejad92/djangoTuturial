from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request,'index.html',context={'message':'Hello, World!'})

def about_us(request):
    return render(request,'about_us.html',context={'message':'Hello, World!'})

def contact_us(request):
    contact_form = ContactForm()
    if(request.method=='POST'):
        name=request.POST['FullName']
        email=request.POST['Email']
        print(name)
        print(email)
    return render(request,'contact_us.html',context={'message':'Hello, World!','contact_form':contact_form})

def login_page(request):
    login_form = LoginForm(request.POST or None)
    if(login_form.is_valid()):
        print(login_form.cleaned_data['username'])
        print(login_form.cleaned_data['password'])
        print(login_form.cleaned_data)
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect('/')
        else:
            print('Something went wrong with login')
    context = {
        'message':'Login Form',
        'name':'msamn',
        'email':'<EMAIL>',
        'login_form':login_form,
    }
    return render(request, 'auth/login.html', context)

def register_page(request):
    context = {
        'message': 'Hello, World!',
        'name': 'msamn',
        'email': '<EMAIL>',
    }
    return render(request, 'auth/register.html', context)