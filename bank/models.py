from django.db import models
from django.forms import ModelForm


class Bank(models.Model):
    name=models.TextField(max_length=50)

class Customer(models.Model):
    SSN=models.CharField(max_length=10)
    CNAME=models.CharField(max_length=50)
    APT_NO=models.PositiveSmallIntegerField()
    STREET_NO=models.PositiveSmallIntegerField()
    CITY=models.CharField(max_length=50)
    STATE=models.CharField(max_length=50)
    ZIP=models.CharField(max_length=10)
    
    def __str__(self):
        return self.CNAME

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['SSN', 'CNAME', 'APT_NO', 'STREET_NO', 'CITY','STATE',
                  'ZIP']


class Loan(models.Model):
    Acc_No = models.PositiveIntegerField()
    Balance = models.PositiveIntegerField()
    
    
    def __str__(self):
        return self.Acc_No

class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = ['Acc_No', 'Balance' ]
