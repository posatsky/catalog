from django.shortcuts import render
from.models import Product



# Create your views here.
def products_lists(request):
    products = Product.objects.all()
    return render(request,'storage/index.html',context={'products':products})


def product_detail(request, slug):
    product= Product.objects.get(slug__iexact=slug)
    return render(request,'storage/product_detail.html',context={'product':product})
