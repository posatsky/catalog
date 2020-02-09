from django.urls import path

from .views import *
#http://127.0.0.1:8080/storage
urlpatterns = [
    path('', posts_lists)
]
