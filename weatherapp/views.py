
from django.shortcuts import render
from weatherapp.forms import *
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse

import urllib.request
import json

# creating the home page

def home(request):
    if request.session.get('username'):
        d={'username':request.session.get('username')}
        return render(request,'home.html',d)
    return render(request,'home.html')

# creating registration page

def registration(request):
    UF=UserForm()
    d={'UF':UF}
    return render(request,'registration.html',d)

# creating the user_login page

def user_login(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        user=authenticate(username=un,password=pw)
        if user and user.is_active:
            login(request,user)
            request.session['username']=un
            return HttpResponseRedirect(reverse('home'))
    if request.method=='POST':
        return render(request,'weatherforcast.html')
        
        

        
    return render(request,'user_login.html')


def user_logout(request):
    logout(request)
    return render(request,'home.html')






# Create your weatherforcast report here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)
        api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=ad6d91c541e7f84004e3201f55d89a05').read()
        api_url2 = json.loads(api_url)

        data = {
            "country": city,
            "weather_description": api_url2['weather'][0]['description'],
            "weather_temperature": api_url2['main']['temp'],
            "weather_pressure": api_url2['main']['pressure'],
            "weather_humidity":api_url2['main']['humidity'],
            "weather_icon": api_url2['weather'][0]['icon'],
        }
        
    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity":None,
            "weather_icon": None,
        }
    print(data['weather_icon'])
    return render(request, 'index.html', {"city": city, "data" :data})
