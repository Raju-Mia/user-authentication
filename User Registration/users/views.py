from django.shortcuts import render, redirect

#my create import
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

#need import for Registration Form With Additional Fields
from .forms import UserRegistrationForm


# Create your views here.

#Default Home page
def home(request):
    return render(request, 'users/home.html')



# #Registration Form or sign up form.
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()

#             messages.success(request, f'Your account has been created. You can log in now!')
#             return redirect('login')

#     else:
#         form = UserCreationForm()

#     context = {'form': form}
#     return render(request, 'users/register.html', context)





#Registration or Sign up Form With Additional Fields
"""By default, the form has a username, password, and password confirmation.
 We will add some additional fields to it. To do 
 so we need to create forms.py inside the users app."""

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')

    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)



#password change funtion
def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('login')

        else:
            form = PasswordChangeForm(user = request.user)
            return render(request, 'users/passwordchange.html', {'form':form})

    else:
        return redirect('login')