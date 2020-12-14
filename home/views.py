from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate,logout, login as log
from django.contrib.auth.decorators import *
from django.http import *
import sqlite3
from django.contrib.auth.models import User
from .forms import RegisterForm,UpdateForm
from django.shortcuts import get_object_or_404
# Create your views here.
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .models import Customer
import logging
import time
from speedtest.speedTest import memberReg
# Create your views here.

logging.basicConfig(level=logging.INFO, filename='logs', filemode='a+', format='utf-8')
def login(request):
    auth = request.user.id
    if (auth):
        return HttpResponseRedirect('/main/')
    form = AuthenticationForm
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        loginControl = AuthenticationForm(data=request.POST)
        if (loginControl.is_valid()):
            user = authenticate(username=username, password=password)
            log(request, user)
            logging.info("sisteme giriş yapildi. Ana sayfaya yönlendiriliyor.")
            return HttpResponseRedirect('/main/')
    return render(request, 'login.html', locals())

def form(request):
    auth = request.user.is_staff
    if not auth:
        return HttpResponseRedirect('/')
    logging.info("kayit sayfasi Acildi")
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        customer = form.save(commit=False)
        name = form.cleaned_data.get('name')
        phoneNumber = form.cleaned_data.get('phoneNumber')
        identificationNumber = form.cleaned_data.get('identificationNumber')
        customer.save()
        logging.info("yeni müsteri basari ile kaydedildi. isim: ",name)
        return HttpResponseRedirect('/main/')

    return render(request, "form.html", {"form": form, 'title': 'Müşteri Kayıt'})

def main(request):
    auth = request.user.is_staff
    if not auth:
        return HttpResponseRedirect('/')
    logging.info(("Anasayfa acildi.").encode('utf-8'))
    customers = Customer.objects.all()
    context = {"Customers":customers}
    logging.info("Müsteriler listelendi")
    return render(request, "main.html",context)

def update(request,id):
    auth = request.user.is_staff
    if not auth:
        return HttpResponseRedirect('/')
    customer = get_object_or_404(Customer,id=id)
    logging.info("güncelleme sayfasi acildi")
    form = UpdateForm(request.POST or None, instance=customer)
    if form.is_valid():
        customer = form.save(commit=False)
        name = form.cleaned_data.get('name')
        phoneNumber = form.cleaned_data.get('phoneNumber')
        identificationNumber = form.cleaned_data.get('identificationNumber')
        customer.save()
        logging.info("bilgiler basarıyla güncellendi. isim:",name)
        logging.info("Anasayfaya yönlendiriliyor")
        return HttpResponseRedirect('/main/')

    return render(request, "update.html", {"form": form, 'title': 'Müşteri Güncelle'})

def delete(request,id):
    auth = request.user.is_staff
    if not auth:
        return HttpResponseRedirect('/')
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    logging.info("Müsteri basariyla silindi. id:",id)
    return HttpResponseRedirect('/main/')

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def speedTest(request):


    start = time.time()

    for a in range(1000):

        name,phoneNumber,identificationNumber=memberReg()
        customer = Customer(name=name, phoneNumber=phoneNumber, identificationNumber=identificationNumber)
        customer.save()

    end = time.time()
    logging.info("test tamamlandi.Sure:", str(end - start))
    return HttpResponseRedirect('/')