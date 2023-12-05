
from django.urls import path 
from . import views

urlpatterns = [
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.register_user,name="register"),
    path('user_profile/',views.user_profile,name="user_profile"),
    path('edit_profile/<int:user_id>/',views.edit_profile,name="edit_profile"),
   
    
    
]