from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

#my create import
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm, AuthenticationForm
from .forms import UserRegistrationForm

#my create import for password change
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


#login required
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    return render(request, 'home.html')

#registration
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


#custom registration
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


#login 
def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data= request.POST)
        if form.is_valid():
            usern = form.cleaned_data['username']
            userp = form.cleaned_data['password']
            user = authenticate(username = usern, password = userp)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'user/login.html', context)



#logout
@login_required(login_url='login')
def logout_form(request):
    logout(request)
    #return redirect('home')
    return render(request, 'user/logout.html')




#passwordchange
@login_required(login_url='login')
def passwordchange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)

                return redirect('login')

        else:
            form = PasswordChangeForm(user=request.user)
            context = {'form':form}
            return render(request, 'user/passwordchange.html', context)

    else:
        return redirect('login')


#passwordchange without old password
@login_required(login_url='login')
def passwordchange_op(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)

                return redirect('login')

        else:
            form = SetPasswordForm(user=request.user)
            context = {'form':form}
            return render(request, 'user/passwordchange_op.html', context)

    else:
        return redirect('login')