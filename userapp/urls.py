from django.urls import path
from .import views
urlpatterns = [
    
    path('', views.index),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('addtocart/<pid>',views.addtocart,name='addtocart'),
    path('email',views.email,name='email')

]