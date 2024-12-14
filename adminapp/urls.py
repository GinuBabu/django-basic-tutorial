from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('adminhome', views.adminhome,name='adminhome'),
    path('allusers', views.allusers,name='allusers'),
    path('delete', views.delete,name='delete'),
    path('edit', views.edit,name='edit'),
    path('update', views.update,name='update'),
    path('upload', views.upload,name='upload'),
    path('productview', views.productview,name='productview'),
  
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 