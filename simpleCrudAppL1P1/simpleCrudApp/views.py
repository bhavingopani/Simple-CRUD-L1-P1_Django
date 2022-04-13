# from ast import Break
# import email
# from multiprocessing import context
from ast import Not
from collections import UserList
from distutils.log import error
from black import err
from django.contrib import messages
from django.shortcuts import redirect, render
from simpleCrudApp.models import CreateUser
from django.contrib.auth import login, logout, authenticate
from cryptography.fernet import Fernet   #for encrypting password
from django.core.paginator import Paginator
from simpleCrudAppL1P1.forms import editforms

# Create your views here.
def index(request):
    # users = CreateUser.objects.all()  #you can directly check this in shell -- what it prints -- with python3 manage.py shell
    # print("email", data)
    # GET THE DATA FROM THE DB And LIST IT.
    # WORK in SPLIT WINDOW 
    # print(data)
    # list_of_teams = Team.objects.filter(team_level__exact="U09")
    # exit()
    user_list = CreateUser.objects.all()
    # print(data)
    # print("email", data)
    # context = {} #as you can pass hear -- context can be used to send data.. and context can be passed in the below render
    # data = {'users' : user_list}
    # breakpoint()
    # return context
    # print (context)
    # exit()
    #SET UP PAGINATION
    p = Paginator(CreateUser.objects.all(), 10)   #takes 2 arguments.. 1. what do we want to paginate for ex. model or the info from database? and 2. How many records per page we want?
    #now we have keep track of the pages. so that each time we click on the next or previous button . we have to track if there are any data or not.
    #for that we use all the methods of paginator function of django
    page = request.GET.get('page') #for getting the page when the requesting that page
    users = p.get_page(page) #the page here is the request metioned above
    #now we have to pass this users varibale same like user_list- we  can do that additionally below
    #NEXT TIME USE OTHER METHODS FOR PAGINATION.
    return render(request, 'authenticate/home.html',
        {'user_list':user_list, 'users':users}) #the home page will list all the details of the user
        #now we dont need the user_list as we are using paginator so changed the way. can pass data via users variable and the same is that of user_list .. so can delete that or can chagne the name of users to user_lsit 


def loginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect('home')
        else:
        # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging in.. please try again"))
            return redirect('loginUser')
    else:
        return render(request, 'authenticate/loginUser.html') #as we dont have any context values or to pass any variaables that you want to pass ahead


    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     user = authenticate(email=email, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect("authenticate/") #redirecting to home page if the user is correct
    #     else:
    #         return render(request, 'authenticate/loginUser.html')
    # return render(request, 'authenticate/loginUser.html')
# START WITH THE LOGOUT BUTTON NOT WORKING --- IT DOES NOT REDIRECT YOU TO OTHER 

def createUser(request):   #next time check django form creation API.
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password=request.POST.get('password') 
        confirm_password= request.POST.get('confirm_password')
        
        #managing validation here in server or View.py .. 
        #Another way to manage validation is in template or html
        error_message = None

        if(not first_name):
            error_message = "First Name is required!!"
        if(not email):
            error_message="Email is required!!"
        if(not password):
            error_message="Password is required!!"
        if(not confirm_password):
            error_message="confirm password is required!!"

        if not error_message:       
            if password == confirm_password:
                key = Fernet.generate_key()
                fernet = Fernet(key)
                password = request.POST.get('password') 
                password = fernet.encrypt(password.encode()) #encyption and encoding of password
                #decryption of password MUST NOT BE USED - its better to use forget password method instead of decypting the password and tell the user that this is your password.
                createuser = CreateUser(first_name=first_name, last_name = last_name, email=email, password=password)    
                messages.success(request, 'Your profile has been created successfully!')    
                createuser.save()
            else:    
                messages.error(request, 'Password and Confirm password must be same')
        else:
            return render(request,'authenticate/createUser.html',{'error': error_message})

    return render(request, "authenticate/createUser.html")

def editUser(request, user_id ): #we are passing user id that we have passed and mentioned in the urls.py 
    #user_list = CreateUser.objects.all() this will grab all from the database but what we want is WE just want respective id and respective record
    #if clicked on edit button
    #here we want primary key or id in the database of the respective record or user that is to be edited
    # user = CreateUser.objects.get(pk=user_id) #pk is the primary key.. and that of user_id - that is coming from the url
                #this basically means.. whatever id you pass in the url .. that will be primary key of that userlist record
    #passing it to the page
    current_user = CreateUser.objects.get(pk=user_id)
    
    return render(request, "authenticate/editUser.html",{'current_user':current_user})

def updateUser(request, user_id):
        
        update_user = CreateUser.objects.get(pk=user_id) #finding the particular database id here.
        form = editforms(request.POST, instance=update_user) #takes two parameter 
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully")
            return render(request, "authenticate/editUser.html",{'current_user':update_user}) 
        
        
        
        # if request.method == "POST":
            
        #     {{current_user}}
        #     # current_user.first_name = first_name
        #     # form = 
        #     # user_id = request.POST.get('id')
        #     first_name = request.POST.get('first_name')
        #     last_name = request.POST.get('last_name')
        #     email = request.POST.get('email')

            
            
        #     current_user = CreateUser(user_id=user_id,first_name=first_name, last_name = last_name, email=email)
        #     current_user.save()

        
        # return redirect("http://127.0.0.1:8000/")
            # return render(request, "authenticate/home.html" )

def deleteUser(request, user_id):
    current_user = CreateUser.objects.get(pk=user_id)   #decidig which one we are going to delete.
    current_user.delete()
    return redirect('home')



def logoutUser(request):
    logout(request)
    return redirect("/loginUser")  #here we are redirecting user to home page or index.html when they logout


# def logoutUser(request):
#     return render(request, )
