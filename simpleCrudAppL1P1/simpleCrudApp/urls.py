from django.contrib import admin
from django.urls import path
from simpleCrudApp import views


urlpatterns = [  #this will send the respective request or matching request to views.py file
    # path('', views.)
    path('', views.index, name="home"),  # ''  here we dont need / as its unnecessary -- as its by default there that is why we dont have / in before any route  So '' this means "http://127.0.0.1:8000/" so no slash of / is required.
    path('loginUser/', views.loginUser, name="loginUser"),   #The first argument to both methods is a route (pattern) that will be matched.
    path('createUser/', views.createUser, name="createUser"),
    # path('editUser/', views.editUser, name="editUser"), #/id can be used here too. will do that later
    path('editUser/<user_id>',views.editUser, name="editUser"),
    path('updateUser/<user_id>',views.updateUser,name="updateUser"),
    path('deleteUser/<user_id>', views.deleteUser,name="deleteUser"),
    # path('activateUser/?email={email}&hashFirst={hashFirst}', views.activateUser, name="activateUser"),
    # path('activateUser/<email>/<hashFirst>/', views.activateUser, name="activateUser"),
    path ('activateUser/<email>/<hashFirst>', views.activateUser, name="activateUser"),
    # path('activateUser/<uidb64>/<token>',views.activateUser, name='activateUser' ),
    # path(   )
 ]

#<> this already means in the urlpatterns that its an argument - and can be used as variables.

# ?email=<email>&hashFirst=<hashFirst>
# ?email={email}&hashFirst={hashFirst}