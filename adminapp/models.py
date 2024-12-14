from django.db import models

# Create your models here.
category_choices=[
    ('wedding','wedding'),
    ('birthday','birthday'),
    ('anniversary','anniversary'),
    ('other','other'),
]

class producttbl(models.Model):
    cakename=models.CharField(max_length=100)
    cakeprice=models.IntegerField()
    cakeimage=models.FileField(upload_to='pictures')
    category=models.CharField(choices=category_choices,default='other',max_length=100)

    def __str__(self):
         return (self.cakename)