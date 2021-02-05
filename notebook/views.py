from django.shortcuts import render


def main_page(request):
    return render(request,'login.html',{})

# Create your views here.
