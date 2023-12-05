from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import RegisterUserForm ,EditProfileForm ,UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,"there was a error login in   ")
            return redirect('login')
    else:
        return render(request,'authentication/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out")
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"registration succesfulll")
            return redirect('login')
    else:
        form = RegisterUserForm()
            
    return render(request,'authentication/register.html',{'form':form,})



@login_required
def user_profile(request):
    user = request.user
    return render(request, 'profile/user_profile.html', {'user': user})

# views.py


@login_required
def edit_profile(request, user_id):
    if not request.user.is_staff:
        # Only allow admin users to access this view
        return redirect('user_profile')  # Redirect to the user's profile page

    # Retrieve the user using the provided user_id
    user_to_edit = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = EditProfileForm(user_to_edit, request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to the user's profile page
    else:
        form = EditProfileForm(instance=user_to_edit)

    return render(request, 'profile/edit_profile.html', {'form': form, 'user_to_edit': user_to_edit})
