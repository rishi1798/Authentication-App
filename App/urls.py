from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('changepass/',views.user_pass_change,name='changepass'),
]
