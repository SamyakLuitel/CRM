from django.contrib import admin
from django.urls import path,include 
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name  ='home'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('products/', views.products, name  ='products'),
    path('create_order/',views.createOrder, name ='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name ='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name ='delete_order'),
]
