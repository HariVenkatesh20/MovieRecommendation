from django.db import models

# Create your models here.
'''class register(models.Model):
    username=models.CharField(max_length=20,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=8)'''


class UserRegister(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
'''class slide(models.Model):
    tit=models.CharField(max_length=20)
    link=models.CharField(max_length=100)
    disc=models.CharField(max_length=200)
    imag=models.ImageField(upload_to = '../media')'''  