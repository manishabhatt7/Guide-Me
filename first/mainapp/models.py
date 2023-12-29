from django.db import models

# Create your models here.


class Guide(models.Model):
  firstname = models.CharField(max_length=255,null=True)
  age = models.IntegerField()
  contact = models.IntegerField()
  gender= models.CharField(max_length=255,null=True)
  address = models.CharField(max_length=255,null=True)
  price = models.IntegerField()
  language = models.CharField(max_length=255,null=True)
  subject=models.TextField()
  