from django.urls import path

from .views import *
#http://127.0.0.1:8080/storage
urlpatterns = [
    path('', products_lists, name= 'products_list_url'),
    path('storage/<str:slug>/', product_detail, name='product_datail_url')
]
