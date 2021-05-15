from django.contrib import admin
from django.urls import path,include 
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name  ='home'),
    path('customer/', views.customer, name='customer'),
    path('products/', views.products, name  ='products'),
]
