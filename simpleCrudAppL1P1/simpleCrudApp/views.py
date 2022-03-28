from django.contrib import messages
from django.shortcuts import render
from simpleCrudApp.models import CreateUser

# Create your views here.
def index(request):
    data = CreateUser.objects.all()
    START WITH ALL THE THINGS like --- PRINTING data and list it on in the templates.
    GET THE DATA FROM THE DB And LIST IT.
    WORK in SPLIT WINDOW 
    print(data)
      
    return render(request, 'home.html') #the home page will list all the details of the user


def loginUser(request):
    return render(request, 'loginUser.html')


def createUser(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password=request.POST.get('password') 
        confirm_password= request.POST.get('confirm_password')
        if password == confirm_password:
            password = request.POST.get('password')    
            createuser = CreateUser(first_name=first_name, last_name = last_name, email=email, password=password)    
            messages.success(request, 'Your profile has been created successfully!')    
            createuser.save()
        else:    
            messages.error(request, 'Password and Confirm password must be same')
    return render(request, "createUser.html")





# def logoutUser(request):
#     return render(request, )