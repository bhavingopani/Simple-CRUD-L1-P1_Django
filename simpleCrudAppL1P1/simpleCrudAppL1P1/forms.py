from attr import fields
from django import forms
from simpleCrudApp.models import CreateUser



class editforms(forms.ModelForm):
    class Meta:
        model = CreateUser
        fields = ['first_name', 'last_name', 'email']  #  it will trough no attribute error if you do not define here.

