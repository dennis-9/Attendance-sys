from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate,login

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages
# Create your views here.

#Homepage
def home(request):
    
    return render(request, 'attendance_webapp/index.html')

#Register
def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "User Account created successfully!")
            return redirect('my-login')
        
    context = {"form": form}
    
    return render(request, 'attendance_webapp/register.html', context=context)
  
  
    
# Login User
def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "User not found. Please register first.")
            return render(request, 'attendance_webapp/my-login.html', context={'form2': form})

        # Authenticate the user
        if not user.check_password(password):
            messages.error(request, "Invalid password")
            return render(request, 'attendance_webapp/my-login.html', context={'form2': form})

        # If user exists and password is correct, log in the user
        login(request, user)
        messages.success(request, "You have logged in successfully.")
        return redirect('dashboard')

    context = {"form2": form}
    return render(request, 'attendance_webapp/my-login.html', context=context)



#Logout            
def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout Success!")

    return redirect('my-login')



#Dashboard
@login_required(login_url='my-login')  
def dashboard(request):
    
    my_records = Record.objects.all()
    
    context = {'records': my_records}
    
    return render(request, 'attendance_webapp/dashboard.html', context=context)


# Add record
@login_required(login_url='my-login')
def add_record(request):
    
    form = AddRecordForm()
    
    if request.method == 'POST':
        
        form = AddRecordForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            #Aunthenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request,user)
            
            messages.success(request, "Your Record was Created!")

            
            return redirect("dashboard")
        
    context = {'form': form}
    
    return render(request, 'attendance_webapp/add_record.html', context=context)

#Update record
@login_required(login_url='my-login')
def update_record(request, pk):
    
    record = Record.objects.get(id=pk)
    
    form = UpdateRecordForm(instance=record)
    
    if request.method == 'POST':
        
        form = UpdateRecordForm(request.POST, instance=record)
        
        if form.is_valid():
            form.save()
            messages.success(request, "You Record was Updated!")

            return redirect("dashboard")
        
    context = {'form': form}
        
    return render(request, 'attendance_webapp/update-record.html', context=context)
    
    
#  Read / View a record
@login_required(login_url='my-login')
def one_record(request, pk):
    if request.user.is_authenticated:
    #Lookup to records
        all_records = Record.objects.get(id=pk)
        
        context={'record': all_records}
        
        return render(request, 'attendance_webapp/view-record.html', context=context)
    else:
        messages.success(request, "You must to be Logged in")


#Delete Record
@login_required(login_url='my-login')
def delete_record(request, pk):
    
    record = Record.objects.get(pk=pk)
    record.delete()
    
    messages.success(request, "Your Record was Deleted!")

    return redirect('dashboard')
    