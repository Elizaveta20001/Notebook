from django.urls import path
from notebook import views

urlpatterns =[
    path('login',views.main_page,name='login')
]