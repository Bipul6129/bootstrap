from django.shortcuts import render

# Create your views here.

def landing_index(request):
    return render(request,'landing/landing_index.html')

def learn_bike(request):
    return render(request,'landing/learn_bike.html')

def learn_car(request):
    return render (request,'landing\learn_car.html')

def learn_excavator(request):
    return render (request,'landing\learn_excavator.html')

def about_us(request):
    return render (request,'landing/about_us.html')
