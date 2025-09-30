# it follows ORM (Object relational mapping) queries set 
# there are methods used for database
# 1) get        = get data
# 2) create     = create object
# 3) filter     = to filter data
# 4) all        = to get all objects

from django.db import models

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