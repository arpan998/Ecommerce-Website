from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='Home'),
    path('login/',views.login, name='login'),
    path('cart/',views.cart, name='cart'),
    path('logout/',views.logout, name='logout')
    
]