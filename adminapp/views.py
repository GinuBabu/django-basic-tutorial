from django.shortcuts import render,redirect
from userapp.models import regtbl
# Create your views here.
def adminhome(request):
    return render(request,'adminhome.html')

def allusers(request):
    alldata=regtbl.objects.all()
    return render(request,'allusers.html',{'users':alldata})

def delete(request):
    idv=request.GET.get('idn')
    obj=regtbl.objects.get(id=idv)
    obj.delete()
    return redirect('/adminapp/allusers')

def edit(request):
    idv=request.GET.get('idn')
    obj=regtbl.objects.get(id=idv)
    return render(request,'edit.html',{'singledata':obj})

def update(request):
     if request.method=='POST':
         idv=request.POST.get('idvalue')
         nm=request.POST.get('name')
         ag=request.POST.get('age')
         em=request.POST.get('email')
         ps=request.POST.get('psw')
         phn=request.POST.get('phone')
         obj=regtbl.objects.get(id=idv)
         obj.name=nm
         obj.age=ag
         obj.email=em
         obj.password=ps
         obj.phone=phn 
         obj.save()  
     return redirect('allusers')

from .models import producttbl
def upload(request):
    if request.method=='POST':
        nm=request.POST.get('cn')
        pr=request.POST.get('cp')
        im=request.FILES.get('img')
        ca=request.POST.get('cat')   
        obj=producttbl.objects.create(cakename=nm,cakeprice=pr,category=ca,cakeimage=im)
        if obj:
              return render(request,'upload.html',{"Success":"product upload scuccessfully"})
        else:
            return render(request,'upload.html',{"error":"product upload failed"})
            

    else:
         return render(request,'upload.html')

    
def productview(request):
    obj=producttbl.objects.all()
    return render(request,'productview.html',{'data':obj}) 