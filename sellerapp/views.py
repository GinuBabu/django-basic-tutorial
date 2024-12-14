from django.shortcuts import render

# Create your views here.
def sellerpage(request):
    return render(request,'sellerpage.html')

def sellerdash(request):
    return render(request,'sellerdash.html')

def managecake(request):
    return render(request,'managecake.html')
