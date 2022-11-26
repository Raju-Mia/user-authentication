#my module
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Registration Form With Additional Fields
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    #Now in views.py we will use UserRegistrationForm instead of the UserCreationForm.
