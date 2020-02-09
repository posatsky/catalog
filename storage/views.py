from django.shortcuts import render



# Create your views here.
def posts_lists(request):
    n=['Oleh','Veasyl','Petro','Misha']
    return render(request,'storage/index.html',context={'names':n})
