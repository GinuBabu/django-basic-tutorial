from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    return render(request,'index.html')
    
from .models import regtbl
def register(request):
    print('inside register')
    if request.method=='POST':
    
       nm=request.POST.get('name')
       ag=request.POST.get('age')
       em=request.POST.get('email')
       ps=request.POST.get('psw')
       pn=request.POST.get('phone')
       try:
          obj=regtbl.objects.create(name=nm,age=ag,email=em,password=ps,phone=pn)

          if obj:
           return render(request,'login.html')
       except:     
           return render(request,'register.html',{'error':"please enter all data"})     

    else:
        return render(request,'register.html')


    
def login(request): 
   if request.method=='POST':
      em=request.POST.get('email')
      ps=request.POST.get('psw')
      obj=regtbl.objects.filter(email=em,password=ps)

      if obj:
         for i in obj:
            request.session['userid']=i.id
            print(i.id,i.name,i.email,i.password )
         # return render(request,'index.html')
            return redirect('/')
      else:
          return render(request,'login.html')
   return render(request,'login.html')

from adminapp.models import producttbl
from .models import carttbl 
from .models import  regtbl


def addtocart(request,pid):
   user=request.session.get('userid')
   cobj=regtbl.objects.get(id=user)
   pobj=producttbl.objects.get(id=pid)
   cartitem,created=carttbl.objects.get_or_create(customer=cobj,product=pobj)
   if not created:
      cartitem.quantity+=1
      cartitem.save()
   return redirect('productview')

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



def email(request):
   if request.method=='POST':
      receiver=request.POST.get('em')
      name=request.POST.get('nm')
      subject="Thank you"
      msg='''
      hi {0} ,
      Thank you for your feedback '''.format(name)
      send_mail(subject,msg,settings.EMAIL_HOST_USER,{receiver},fail_silently=False)
      messages.success(request,"mail sended successfully")
      return redirect('email')
   else:
      return render(request,'email.html')

