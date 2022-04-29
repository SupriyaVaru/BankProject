from django.contrib import admin
from .models import Bank,Customer,Loan

# Register your models here.
admin.site.register(Bank)
admin.site.register(Customer)
admin.site.register(Loan)