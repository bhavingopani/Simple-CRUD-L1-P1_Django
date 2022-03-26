from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')


def loginUser(request):
    return render(request, 'loginUser.html')


def createUser(request):
    return render(request, 'createUser.html')



# def logoutUser(request):
#     return render(request, )