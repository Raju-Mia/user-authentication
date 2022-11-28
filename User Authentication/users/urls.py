
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views



urlpatterns = [
    path('', user_views.home, name='home'),

    #registration url
    path('register/', user_views.register, name='register'),
    path('customregister/', user_views.custom_register, name='customregister'),

    #login url
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),

    #logout url
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

    #pasword change url
    path('passwordchange/', user_views.passwordchange, name='passwordchange'),

     #pasword change without old password url
    path('passwordchangewo/', user_views.passwordchange_op, name='passwordchangewo'),
]
