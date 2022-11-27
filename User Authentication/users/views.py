from django.shortcuts import render, redirect
from django.contrib import messages

#my create import
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm




# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request,"user/register.html", context)



def custom_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')

    else:
        form = UserRegistrationForm()

    context = {'form':form}
    return render(request,"user/custom_register.html", context)