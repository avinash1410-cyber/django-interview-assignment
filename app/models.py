from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    position= models.CharField(max_length=20,blank=True, null=True)

    @property
    def is_librarian(self):
        return self.position=="Librarian"



class Book(models.Model):
    Name = models.CharField(max_length=200,null=True,blank=True)
    Status=models.CharField(max_length=200,null=True,blank=True)
    Owner=models.OneToOneField(Account,null=True,blank=True,on_delete=models.SET_NULL)


