from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect

def main_page(request):
    if request.user.is_authenticated:
        return render(request,'start_page.html',{})
    else:
        return render(request,'login.html',{})

def authentication(request):
    user = authenticate(
        username=request.POST["username"],
        password=request.POST["password"]
    )
    if user is None:
        return render(request,"error.html",{})
    else:
        login(request,user)
        return HttpResponseRedirect("/")
# Create your views here.
