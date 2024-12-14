from django.urls import path
from .import views

urlpatterns = [
    
    path('sellerpage', views.sellerpage,name='sellerpage'),
    path('sellerdash', views.sellerdash,name='sellerdash'),
    path('managecake', views.managecake,name='managecake'),

  
    
]