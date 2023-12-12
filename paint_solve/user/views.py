from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import  EditProfileForm ,UserChangeForm,RegisterUserForm
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



# def register_user(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')
        
#         if pass1!=pass2:    
#             return HttpResponse("Your password and confirm password are not same!!!")
#         else:
#             my_user=User.objects.create_user(uname,email,pass1)
#             my_user.save()
           
#             return redirect('login')
           
#     return render(request,'authentication/register.html')
    

# def register_user(request):
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username,password=password)
#             login(request,user)
#             messages.success(request,"registration succesfulll")
#             return redirect('login')
#     else:
#         form = RegisterUserForm()
            
#     return render(request,'authentication/register.html',{'form':form,})


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, "Registration successful")
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please correct the errors in the form.")
    else:
        form = RegisterUserForm()
    
    return render(request, 'authentication/register.html', {'form': form})



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
