from django.urls import path
from notebook import views

urlpatterns =[
    path('',views.main_page,name='login'),
    path('authencation',views.authentication,name='authencation')
]