from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth import login,logout
from .models import *
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def index(request):
    parms = {
        'headtitle': 'Suvana | SEARCH PRODUCTS',
    }
    user = request.user
    if user.is_authenticated:
        q = request.GET.get('q')
        if q is None:
            q = ' '
        products = product.objects.filter(
            Q(size__icontains = q) |
            Q(modelno__icontains = q) |
            Q(water__icontains = q) |
            Q(gas__icontains = q) |
            Q(air__icontains = q) |
            Q(wpf__icontains = q) |
            Q(density__icontains = q) |
            Q(vescosity__icontains = q) |
            Q(temp__icontains = q) |
            Q(pressure__icontains = q) |
            Q(distance__icontains = q) |
            Q(price__icontains = q)
            ).distinct()

        parms = {
            'products':products,
            'headtitle': 'Suvana | SEARCH PRODUCTS',
            }
    return render(request, 'index.html', parms)


def about(request):
    head = "PMS | ABOUT"
    parms = {
        'head':head,
    }
    return render(request, 'about.html', parms)

def login(request):
    head = "Product Suvana | LOGIN"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            send_mail(
                'User Logged In',
                username,
                'ekesel05@gmail.com',
                ['sales1@suvana.co.in'],
                fail_silently=False,
            )
            messages.info(request,'Logged In Successfully')
            return redirect('index')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'login.html',{'head':head})

def logouts(request):
    logout(request)
    return redirect('login')

