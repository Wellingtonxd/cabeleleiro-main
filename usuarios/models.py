from django.db import models

# Create your models here.

class Ruan(models.Model):
     username=models.CharField(primary_key=True, max_length=20)
     senha=models.CharField(max_length=20)
     email=models.CharField(max_length=30)


     def __str__(self):
         texto="{0} ({1})"
         return texto.format(self.email,self.username)
