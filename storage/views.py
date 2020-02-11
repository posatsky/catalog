from django.shortcuts import render
from.models import Product



# Create your views here.
def posts_lists(request):
    products = Product.objects.all()
    return render(request,'storage/index.html',context={'products':products})
