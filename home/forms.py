from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Customer
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
import logging

##logging.basicConfig(filename="form.log", level=logging.INFO)
logging.basicConfig(level=logging.INFO, filename='logs', filemode='a+', format='[%(asctime)-15s] %(levelname)-8s %(message)s')

class RegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Name, Surname')
    phoneNumber = forms.CharField(max_length=11, validators=[RegexValidator(r'^\d{11,11}$')], label='Phone Number')
    identificationNumber = forms.CharField(max_length=11, validators=[RegexValidator(r'^\d{11,11}$')], label='Identification Number')

    class Meta:
        model = Customer
        fields = [
            'name',
            'phoneNumber',
            'identificationNumber',
        ]
    def clean_identificationNumber(self):
        identificationNumber=self.cleaned_data.get("identificationNumber")
        identificationNumber=int(identificationNumber)
        ctrlIde = Customer.objects.filter(identificationNumber=identificationNumber).values()
        ctrlIde=len(ctrlIde)
        if int(identificationNumber)<10000000000:
            logging.info("Kimlik numarasi uygun degil.")
            raise forms.ValidationError("Kimlik numarası uygun değil.")

        if ctrlIde>0:
            logging.info("Kimlik numarasi kayitli.")
            raise forms.ValidationError("Kimlik numarası kayıtlı.")
        return identificationNumber


class UpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Name, Surname')
    phoneNumber = forms.CharField(max_length=11, validators=[RegexValidator(r'^\d{11,11}$')], label='Phone Number')
    identificationNumber = forms.CharField(max_length=11, validators=[RegexValidator(r'^\d{11,11}$')], label='Identification Number')

    class Meta:
        model = Customer
        fields = [
            'name',
            'phoneNumber',
            'identificationNumber',
        ]
    def clean_identificationNumber(self):
        identificationNumber=self.cleaned_data.get("identificationNumber")
        identificationNumber=int(identificationNumber)
        ctrlIde = Customer.objects.filter(identificationNumber=identificationNumber).values()
        ctrlIde=len(ctrlIde)
        if int(identificationNumber)<10000000000:
            logging.info("Kimlik numarasi uygun degil.")
            raise forms.ValidationError("Kimlik numarası uygun değil.")

        return identificationNumber







