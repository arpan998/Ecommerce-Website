from django.shortcuts import render, redirect
from django.http import request,HttpResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

# Create your views here.

def home(request):
    
      return render(request, 'e-com.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.POST
        if "submit" in data:
            username = data.get('username')
            password = data.get('password')
            user = auth.authenticate(username=username,password=password)
            if user is not None:
               auth.login(request,user)
               return redirect('cart')
        

    return render(request, 'login.html')

@csrf_exempt
def cart(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            data = request.GET
            if 'submit' in data:
                Name= data.get('name')
                Email= data.get('email')
                Address=data.get('add')
                Mobile= data.get('mob')
                State= data.get('state')
                City= data.get('city')
                Pin= data.get('pin')
                Landmark= data.get('lm')

                submit = models.Address(Name=Name, Email=Email, Address=Address, Mobile=Mobile, State=State, City=City, Pin=Pin, Landmark=Landmark)
                submit.save()
                return redirect('cart')
        #return HttpResponse(' Your order successfully Placed !')
        return render(request,'cart.html')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect(login)
    

    

