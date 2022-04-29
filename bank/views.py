from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View,ListView,TemplateView
from django.urls import reverse
from bank.models import CustomerForm, Customer, Loan, LoanForm


import os
import cx_Oracle
# Create your views here.

def login(request):
    return render(request, 'bank/login.html')

def home(request):
    return render(request, 'bank/base.html')

def insert(request):
    customers = list(Customer.objects.all())
    val = customers[len(customers) -1]
    val1 = []
    #val2 = []
    #val3 = []
    #val4 = []
    #val5 = []
    #val6 = []
    #val7 = []
    #scredit = []
    #scourse = []
    #for val in context:
    # val1.append(val.SSN)
    # val1.append(val.CNAME)
    # val1.append(val.APT_NO)
    # val1.append(val.STREET_NO)
    # val1.append(val.CITY)
    # val1.append(val.STATE)
    # val1.append(val.ZIP)
    custd=[val.SSN, val.CNAME,val.APT_NO,val.STREET_NO,val.CITY,val.STATE,val.ZIP]
    print(custd)
    print('this is taken from form')
    dsn = cx_Oracle.makedsn("prophet.njit.edu", 1521, sid="course")
    conn = cx_Oracle.connect(user="sv247", password="BlueTucson@2022", dsn=dsn, encoding="UTF-8")
        

    print('Successfully connected to Oracle Database')

    #Retrieve Data
    cursor=conn.cursor()
    print('step1')
    #query=self.request.GET.get("q")
    rows= [val.SSN, val.CNAME,val.APT_NO,val.STREET_NO,val.CITY,val.STATE,val.ZIP]
    print('step2')
    print(rows[0])
    #insert='''insert into customers 
               # values (1313137777, 'SAI',1,1,'harrison','NJ','07029')'''
    cursor.execute('insert into customers (SSN,CNAME,APT_NO,STREET_NO,CITY,STATE,ZIP) values (:1,:2,:3,:4,:5,:6,:7)',rows)
    print('step3')
        #account=[]
        #Sbalance=[]
        #Sfixed_int_rt=[]
    print(cursor.rowcount,'insert executed')

    conn.commit()
    query=rows[0]
    select="select * from customers where SSN IN ("+query+")"
    cursor.execute(select)
    
    for value in cursor:
            
            #act1=[acc_no[0],acc_no[1],acc_no[2]]
            
            customer_details =   {'SSN': value[0], 
                                'CNAME': value[1],
                                'APT_NO': value[2],
                                'STREET_NO': value[3],
                                'CITY':value[4],
                                'STATE':value[5],
                                'ZIP':value[6],
                                }
                                
            print(value[0])
            print(value[1])
            print(value[2])
            print(value[3])
            print(value[4])
   
            #account.append(act1)
            #Sbalance.append(balance)
            #Sfixed_int_rt.append(fixed_int_rt)
                
 
        #savings_act = {'account':account}
    print(customer_details)

        #act2="hello" 
                  
    conn.close() 
        
    return render(request, 'bank/insert_results.html', customer_details)

def AddCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            print('formsaved')
            return HttpResponseRedirect(reverse('insert'))
    else:
        form = CustomerForm()
    
    return render(request, 'bank/customer.html', {'form': form})



class DB(TemplateView):
    #def get(self, request, *args, **kwargs):

        #savings_act = get_data()
    template_name= 'bank/savings.html'

class SearchResultsView(ListView):
    #template_name= 'bank/search_results.html'
    def get(self, request, *args, **kwargs):

        savings_act = get_queryset(self)
        return render(request, 'bank/search_results.html',savings_act)


def get_queryset(self):
        #conn = cx_Oracle.connect('sv247/BlueTucson@2022@prophet.njit.edu')
        dsn = cx_Oracle.makedsn("prophet.njit.edu", 1521, sid="course")
        conn = cx_Oracle.connect(user="sv247", password="BlueTucson@2022", dsn=dsn, encoding="UTF-8")
        

        print('Successfully connected to Oracle Database')

        #Retrieve Data
        cursor=conn.cursor()
        query=self.request.GET.get("q")
        select='''select a.acc_no,CName,balance,fixed_int_rt,bname,most_recentdate
                  from branches b join 
                  account a  on b.branch_id=a.branch_id join
                  customers c on c.ssn=a.cssn join
                  savings_acct s on a.acc_no=s.acc_no 
                  where s.acc_no in ('''+query+')'
        print(query)
        cursor.execute(select)
        #account=[]
        #Sbalance=[]
        #Sfixed_int_rt=[]
        print(cursor)
        for value in cursor:

            #act1=[acc_no[0],acc_no[1],acc_no[2]]
            d=str(value[5])
            
            account_details =   {'acc_no': value[0], 
                                'CName': value[1],
                                'balance': value[2],
                                'fixed_int_rt': value[3],
                                'bname':value[4],
                                'most_recentdate':d[:-8]}
            print(value[0])
            print(value[1])
            print(value[2])
            print(value[3])
            print(value[4])
            print(value[5])
   
            #account.append(act1)
            #Sbalance.append(balance)
            #Sfixed_int_rt.append(fixed_int_rt)
                
 
        #savings_act = {'account':account}
        print(account_details)

        #act2="hello" 
                  
        conn.close() 
        return account_details

def update(request):
    balance = list(Loan.objects.all())
    val = balance[len(balance) -1]
    
    loand=[val.Acc_No, val.Balance]
    print(loand)
    print('this is taken from loanform')
    dsn = cx_Oracle.makedsn("prophet.njit.edu", 1521, sid="course")
    conn = cx_Oracle.connect(user="sv247", password="BlueTucson@2022", dsn=dsn, encoding="UTF-8")
        

    print('Successfully connected to Oracle Database')

    #Retrieve Data
    cursor=conn.cursor()
    print('step1')
    
    rows= [val.Acc_No, val.Balance]
    print('step2')
    print(rows[0])
    valid="select ACC_NO from Loan_acct"
    cursor.execute(valid)
    for i in cursor:
        print(i[0])
        if i[0] == rows[0]:
            print('match found')
        


            update="update Loan_acct SET Balance = "+str(rows[1])+" where ACC_NO IN "+str(rows[0])+""
            cursor.execute(update)
            print('step3')
        
            print(cursor.rowcount,'update executed')

            conn.commit()
            query=rows[0]
            select="select * from Loan_acct where ACC_NO IN ("+str(query)+")"
            cursor.execute(select)
            
            for value in cursor:
                    
                            
                    account_details =   {'ACC_NO': value[0], 
                                        'BALANCE': value[1],
                                        'FIXED_INT_RT': value[2],
                                        'TYPE': value[3],
                                        'AMOUNT':value[4],
                                        'MONTHLY_REPAY':value[5],
                                        'BRANCH_ID':value[6],
                                        'COMMENT': "Successful",
                                        }
                                        
                    print(value[0])
                    print(value[1])
                    print(value[2])
                    print(value[3])
                    print(value[4])
        else:
            print('match not found')
            account_details =   {'ACC_NO': "NA", 
                                        'BALANCE': "NA",
                                        'FIXED_INT_RT': "NA",
                                        'TYPE': "NA",
                                        'AMOUNT':"NA",
                                        'MONTHLY_REPAY':"NA",
                                        'BRANCH_ID':"NA",
                                        'COMMENT': "Error || Account Not Found",
                                        }
            
    print(account_details)
 
                  
    conn.close() 
        
    return render(request, 'bank/update_results.html', account_details)

def LoanAcct(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            print('formsaved')
            return HttpResponseRedirect(reverse('update'))
    else:
        form = LoanForm()
    
    return render(request, 'bank/loan.html', {'form': form})




