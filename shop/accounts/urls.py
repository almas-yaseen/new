from django.urls import path
from .import views  
urlpatterns = [
  path('login/',views.login,name='login'),
  path('register/',views.register,name='register'),
  path('logout/',views.logout,name='logout'),
  path('activate/<uidb64>/<token>/',views.activate,name='activate'),
  path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate,name='resetpassword_validate'),
  path('dashboard/',views.dashboard,name='dashboard'),
  path('',views.dashboard,name='dashboard'),
  path('forgotPassword/',views.forgotPassword,name='forgotPassword'),
path('resetPassword/',views.resetPassword,name='resetPassword'),
path('my_orders/',views.my_orders,name='my_orders'),
path('edit_profile/',views.edit_profile,name='edit_profile'),
path('change_password/',views.change_password,name='change_password'),
    
]
