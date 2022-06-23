from django.db import models

# Create your models here.
class AutisticData(models.Model):
    sno=models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    address = models.TextField()
    gender=models.CharField(max_length=20)
    refferedBy= models.CharField(max_length=50)
    
    # Birth history
    birthDate=models.DateField()
    birthWeight=models.IntegerField()
    term=models.CharField(max_length=20)
    delivery=models.CharField(max_length=20)
    consanguinity=models.CharField(max_length=20)
    perninantalEvents=models.CharField(max_length=20)
    term=models.CharField(max_length=20)
    treatment=models.CharField(max_length=20)
    
    