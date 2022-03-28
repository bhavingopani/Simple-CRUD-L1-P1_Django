from django.contrib import admin
from django.urls import path
from simpleCrudApp import views

urlpatterns = [
    # path('', views.)
    path('', views.index, name="home"),
    path('loginUser', views.loginUser, name="loginUser"),
    path('createUser', views.createUser, name="createUser"),

]

# START WITH WHY createUser is not working first... Then go ahead with all ,., like creating superuser and user Django Admin , models and all.
# ALSO FIRST CHANGE THE BRANCH AND COPY ALL FROM MASTER TO MAIN... AND DELETE THE MASTER BRANCH.