

from django.db import models
# from django.cryptography.fields import encrypt
# Create your models here.


class CreateUser(models.Model):  #the below all null and blank is not at the database validation -- that can be done when we use form validation API.
                                #another way to validate is on Server and in HTML page -- server means in views.py .. another is in template.
    first_name = models.CharField(max_length=122) #this means it can not be null  - null is at database level and blank is at validation level. Always check how its reuired
    last_name = models.CharField(max_length=122)
    email= models.CharField(max_length=122,unique=True) #Email address must be unique
    hash = models.CharField(max_length=200, default='') #should be matched with the link sent in the email. #default is needed as we are adding the field to an existing model
    email_status = models.CharField(max_length=122, default='')
    password= models.CharField(max_length=122)    #installed cryptography librabry to encrypt the password.
    # confirm_password = models.CharField(max_length=122) not needed as its no longer needed after sign up is done by the user.
    # NULL vs EMPTY   -- NULL and EMPTY string has a vast difference.
    # def __str__(self) -> str:
    #     return self.first_name #this is for django admin panel -- so that it will display as the first_name insted of object


    
class Home(models.Model): #user details listing.
    full_name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    email_status = models.CharField(max_length=122)

    # def __str__(self) -> str:
    #     return self.full_name #this is for django admin panel -- so that it will display as the full_name insted of object

