from django.contrib import admin
from simpleCrudApp.models import CreateUser, Home

# Register your models here.
admin.site.register(CreateUser) #once its registered it will be displayed in the django admin panel.
admin.site.register(Home)
 