from django.contrib import admin
from django.urls import path
from userauth import views  
from userauth.views import destination_view
from userauth.views import home_view, contact_view  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  
    path('about/', views.about_view, name='about'),  
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('destination/', destination_view, name='destination'),
    path('contact/', contact_view, name='contact'),
    path('Destinations', views.destination_view, name='destination_alt'),  # New alias
    path('cultural-experiences/', views.cultural_experiences, name='cultural-experiences'),
    path('itinerary-planner/', views.itinerary_planner, name='itinerary-planner'),
    path('sustainable-travel/', views.sustainable_travel, name='sustainable-travel'),

]

