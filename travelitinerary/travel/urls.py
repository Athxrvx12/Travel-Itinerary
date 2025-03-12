# from django.contrib import admin
# from django.urls import path
# from travel import views

# urlpatterns = [
#     path("",views.index, name="travel"), 
# ]
from django.urls import path
from .views import signup_view, login_view, logout_view, views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('destination/', destination_view, name='destination'),
]



