from django.urls import path
from .import views  
urlpatterns = [
  path('login/',views.login,name='login'),
  path('register/',views.register,name='register'),
  path('logout/',views.logout,name='logout'),
  path('activate/',views.activate,name='activate'),
    
]
