
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views



urlpatterns = [
    path('', user_views.home, name='home'),

    #registration url
    path('register/', user_views.register, name='register'),
    path('customregister/', user_views.custom_register, name='customregister'),
]
