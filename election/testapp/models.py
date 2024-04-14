from django.db import models

# Create your models here.

class VoterModel(models.Model):
    sno=models.IntegerField()
    name=models.CharField(max_length=30)
    fatname=models.CharField(max_length=30)
    epic=models.CharField(max_length=20)
    addr=models.CharField(max_length=50)
    phone=models.BigIntegerField()
