from django.contrib import admin
from django.urls import path
from simpleCrudApp import views

urlpatterns = [
    # path('', views.)
    path('', views.index, name="home"),
    path('login', views.loginUser, name="loginUser"),
    path('logout', views.createUser, name="createUser"),

]

START WITH WHY createUser is not working first... Then go ahead with all ,., like creating superuser and user Django Admin , models and all.