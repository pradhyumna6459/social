from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup',views.signup,name='signup'),
    path('Register',views.Register,name='Register'),
    path('home',views.home,name="home"),
    path('logout',views.logout,name='logout'),
    path('afterlogin',views.afterlogin,name='afterlogin'),
    path('contact',views.contact,name='contact'),
    path('meetTheTeam',views.meetTheTeam,name='meetTheTeam'),
    path('ngo',views.ngo,name='ngo'),
]
