from django.urls import URLPattern, path, include
from . import views

urlpatterns = [
   
    path('DB', views.DB.as_view(),name='DB'),
    path('search', views.SearchResultsView.as_view(), name="search_results"),
    path('login', views.login, name='login' ),
    path('home', views.home, name='home' ),
    path('customer',views.AddCustomer,name='CustomerForm'),
    path('insert', views.insert, name='insert'),
    path('loan',views.LoanAcct,name='LoanAcct'),
    path('update', views.update, name='update'),
    
    
    

]