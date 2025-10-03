# it follows ORM (Object relational mapping) queries set 
# there are methods used for database
# 1) get        = get data
# 2) create     = create object
# 3) filter     = to filter data
# 4) all        = to get all objects

from django.db import models
from datetime import time

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mno = models.BigIntegerField(unique=True)           # mobile number
    password = models.CharField(max_length=20)
    profile = models.ImageField(default="")
    usertype = models.CharField(max_length=20, default="pateint")   

    def __str__(self):
        return f"{self.name}" 


class Doctor(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    category = (
            ("Dermatologist", "Dermatologist"),
            ("Neurologist", "Neurologist"),
            ("Surgeon", "Surgeon"),
            ("Immunology", "Immunology")
        )
    
    cchoice = models.CharField(max_length=20, choices=category)
    dname = models.CharField(max_length=20)
    demail = models.EmailField(unique=True)
    qfc = models.CharField(max_length=40)
    charges = models.IntegerField()
    address = models.TextField()
    dtime = models.TimeField(default=time(9, 0))
    dctime = models.TimeField(default=time(9, 0))
    exp = models.IntegerField()
    dimage = models.ImageField(default="", upload_to='doctor/')

    def __str__(self):
        return f"{self.doctor}"