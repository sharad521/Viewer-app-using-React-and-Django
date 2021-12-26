from django.db import models

# Create your models here.
class Task(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    age = models.IntegerField()
    content= models.CharField(max_length=10000000)

    def __str__(self):
        return self.FirstName

class About(models.Model):
    FirstName = models.CharField(max_length=15000)
    LastName = models.CharField(max_length=1500)
    address = models.CharField(max_length=150000)
    age = models.IntegerField()
    gender =  models.CharField(max_length=150)  
    qualification =  models.CharField(max_length=15000)   
    birthplace=  models.CharField(max_length=15000)  
    maritalstatus=  models.CharField(max_length=1500)  
    interestinggame=  models.CharField(max_length=1500) 
    interestingcountry=  models.CharField(max_length=15000) 
         

    def __str__(self):
        return self.FirstName