from django.contrib import messages
from django.shortcuts import redirect, render
from simpleCrudApp.models import CreateUser
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    users = CreateUser.objects.all()  #you can directly check this in shell -- what it prints -- with python3 manage.py shell
    # print("email", data)
    # GET THE DATA FROM THE DB And LIST IT.
    # WORK in SPLIT WINDOW 
    # print(data)
      
    return render(request, 'home.html',{'users':users}) #the home page will list all the details of the user


def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/") #redirecting to home page if the user is correct
        else:
            return render(request, 'loginUser.html')
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


def logoutUser(request):
    logout(request)
    return redirect("/loginUser.html")  #here we are redirecting user to home page or index.html when they logout


# def logoutUser(request):
#     return render(request, )