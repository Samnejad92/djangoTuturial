from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',context={'message':'Hello, World!'})

def about_us(request):
    return render(request,'about_us.html',context={'message':'Hello, World!'})

def contact_us(request):
    if(request.method=='POST'):
        name=request.POST['FullName']
        email=request.POST['Email']
        print(name)
        print(email)
    return render(request,'contact_us.html',context={'message':'Hello, World!'})