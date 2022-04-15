# from ast import Break
# import email
# from multiprocessing import context
# from ast import Not
# from collections import UserList
# from distutils.log import error
# from black import err
from distutils.log import error
from attr import has
from django.contrib import messages
from django.shortcuts import redirect, render
from simpleCrudApp.models import CreateUser
from django.contrib.auth import login, logout, authenticate
from cryptography.fernet import Fernet   #for encrypting password
from django.core.paginator import Paginator
from simpleCrudAppL1P1.forms import editforms
from django.core.mail import send_mail
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from .tokens import account_activation_token
# from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
# from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth import get_user_model
# from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate
import random
from django.utils.crypto import get_random_string


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


        # hash =    random.randint(0,1000)
        hashFirst = get_random_string(length=32)
        email_status = "pending"
        #the below is for checking if the email exists. we have to check if the email is already there in the database.
        user_list = CreateUser.objects.all()

        #managing validation here in server or View.py .. 
        #Another way to manage validation is in template or html
        error_message = None
        
        for user in user_list:
            if email == user.email:
                error_message = "Email already exists in the system!"
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
                createuser = CreateUser(first_name=first_name, last_name = last_name, email=email, password=password, hash=hashFirst, email_status=email_status)    
                messages.success(request, 'Your profile has been created successfully!')
                    
                createuser.save()
                
                
                #after saving is done. Sending an email without token first. Token we will use to verify the email.
                email_subject = 'Activate Your Email Account'
                # for user in user_list:   #
                email_message = f'Please click this link to activate your account  http://127.0.0.1:8000/activateUser/{email}/{hashFirst}'
                #http://127.0.0.1:8000/activateUser/?email={email}&hashFirst={hashFirst}
                to_email = email        
                
                send_mail(       #if we want some advanced features like cc , bcc and attatchements., we can use EmailMessage of django
                    email_subject, #subject
                    email_message, #message
                    'testpatel456@gmail.com', #from email
                    [to_email, 'gopani7874@gmail.com'], #to email #always in array
                    fail_silently= False, #A boolean. When it’s False, send_mail() will raise an smtplib.SMTPException if an error occurs. See the smtplib docs for a list of possible exceptions, all of which are subclasses of SMTPException.
                )

                # print(email, hashFirst)
                # user=createuser.save()
                # user.is_active = False
                # current_site = get_current_site(request)
                # email_subject = 'Activate Your Account'
                # email_message = render_to_string('email_template.html', {
                #                     'user':user,
                #                     'domain': current_site.domain,
                #                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                #                     'token': account_activation_token.make_token(user),
                #              })
                # to_email = request.POST.get('email')
                # send_mail(email_subject, email_message,'testpatel456@gmail.com',[to_email])

            else:    
                messages.error(request, 'Password and Confirm password must be same')
        else:
            return render(request,'authenticate/createUser.html',{'error': error_message})

    return render(request, "authenticate/createUser.html")

def activateUser(request, email, hashFirst):
    #now matching the hash from the email activation link and the respective hash code from the link
    if request.method == "GET":
        # emailNew = request.GET.get('email')
        # hashFirstNew = request.GET.get('hashFirst')
        
        user_list = CreateUser.objects.all()
        for user in user_list:
            # print(user.hash)
            if user.email == email and user.hash == hashFirst:
            # if user.email == email: 
            # and user.hash == hashFirst:
                # message = "Your account has been activated successfully!!"
                user.email_status = "verified"
                user.save() # this will update the same.
                # return render(request, 'authenticate/activateUser.html',{'message':message})
                # return redirect('home', {'message':message})
                # return render(request, 'authenticate/home.html',{'message':message})
                messages.success(request, 'Your account has been activated successfully!!')
                return redirect('home')
            else:
                messages.error(request, 'Sorry!! Your account could not be verified. Please contact us at testpatel456@gmail.com')
                # messages.error = "Sorry!! Your account could not be verified. Please contact us at testpatel456@gmail.com"
                # return render(request, 'authenticate/activateUser.html',{'message':message})
                # return redirect('home', {'message':message})
                # return render(request, 'authenticate/home.html',{'message':message})
                return redirect('home')





# def activateUser(request, uidb64, token):
#     User = get_user_model()
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')





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
            new_updated_user=CreateUser.objects.get(pk=user_id)
            if update_user.email != new_updated_user.email and update_user.email_status == "verified" :
                new_updated_user.email_status = "pending"
                new_updated_user.save()

WRITE DOWN THE LOGIC AGAIN --- FOR REVERIFICATION and ALL -- CHECK EDIT after the FORM IS VERIFIED>


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




# def activateUser(request,uidb64,token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # return redirect('home')
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')
#     # return render('home')





def deleteUser(request, user_id):
    current_user = CreateUser.objects.get(pk=user_id)   #decidig which one we are going to delete.
    current_user.delete()
    return redirect('home')







def logoutUser(request):
    logout(request)
    return redirect("/loginUser")  #here we are redirecting user to home page or index.html when they logout


# def logoutUser(request):
#     return render(request, )
