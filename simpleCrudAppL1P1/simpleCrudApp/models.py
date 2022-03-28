from base64 import encode
from django.db import models
# from django.cryptography.fields import encrypt

# Create your models here.

class CreateUser(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    password= models.CharField(max_length=122)    #installed cryptography librabry to encrypt the password.
    # confirm_password = models.CharField(max_length=122) not needed as its no longer needed after sign up is done by the user.

    def __str__(self) -> str:
        return self.first_name #this is for django admin panel -- so that it will display as the first_name insted of object
    
class Home(models.Model): #user details listing.
    full_name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    email_status = models.CharField(max_length=122)

    def __str__(self) -> str:
        return self.full_name #this is for django admin panel -- so that it will display as the full_name insted of object

