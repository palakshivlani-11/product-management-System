from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth import login,logout
from .models import *
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import mail_admins

# Create your views here.
def index(request):
    parms = {
        'headtitle': 'Suvana | SEARCH PRODUCTS',
    }
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            cat = request.POST['cat']
            sizes = request.POST['sizes']
            print('Hello')
            return redirect('filtered',cat=cat,sizes=sizes)
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


def filtered(request,cat,sizes):
    parms = {
        'headtitle': 'Suvana | SEARCH PRODUCTS',
    }
    user = request.user
    if user.is_authenticated:
        q = request.GET.get('q')
        if q is None:
            q = ' '
        products = product.objects.filter(
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
        filterprods = []
        for prods in products:
            if prods.category == cat and prods.size == sizes:
                filterprods.append(prods)
        parms = {
            'filterprods':filterprods,
            'headtitle': 'Suvana | SEARCH PRODUCTS',
        }
    return render(request, 'filter.html', parms)

def details(request,id):
    try:
        prod = product.objects.get(pk=id)
    except:
        raise Http404("Product Does Not Exist")

    parms = {
        'prod':prod,
        'headtitle': prod.modelno,
    }
    return render(request,'details.html',parms)

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
            msg = "Username - "+username+" Logged in!"
            res = mail_admins('NEW LOGIN', msg)
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

