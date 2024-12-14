from django.db import models
from adminapp.models import producttbl
# Create your models here.
class regtbl(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)
    phone=models.IntegerField()

class carttbl(models.Model):
    customer=models.ForeignKey(regtbl,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(producttbl,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
