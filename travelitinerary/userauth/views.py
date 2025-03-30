# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.models import User
# from django.http import HttpResponse

# def home_view(request):
#     return render(request, 'home.html')  # ✅ Make sure home.html exists

# def login_view(request):
#     return HttpResponse("Login Page")  # Replace with actual login logic

# def signup_view(request):
#     return HttpResponse("Signup Page")  # Replace with actual signup logic

# def logout_view(request):
#     logout(request)
#     return redirect('home')
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')  # ✅ Ensure this function exists

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def destination_view(request):
    return render(request, 'destination.html')

def contact_view(request):
    return render(request, 'contact.html')

def itinerary_planner(request):
    return render(request, 'itinerary_planner.html')

def cultural_experiences(request):
    return render(request, 'cultural_experiences.html')

def sustainable_travel(request):
    return render(request, 'sustainable_travel.html')

def plan_trip(request):
    return render(request, 'plan_trip.html')