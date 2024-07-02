from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from myApp.forms import RegistrationForm,LoginForm


# Create your views here.

# function for rendering home page
def home(request):
     return render(request,'myApp/home.html')


def registrationView(request):
     if request.method == 'POST':
          form=RegistrationForm(request.POST)
          if form.is_valid():
               user=form.save()
               login(request,user)
               messages.success(request,"registration successfully")
               # return redirect("home")
     else:
          form=RegistrationForm()
     return render(request,'myApp/register.html',{'form':form}) 

def loginView(request):
     if request.method == 'POST':
          form=LoginForm(data=request.POST)   
          if form.is_valid():
               uname=form.cleaned_data['username']
               upass=form.cleaned_data['password']
               user=authenticate(username=uname,password=upass) 

               if user is not None:
                    login(request,user)
                    messages.success(request,'login Successfully')
                    return redirect('login')
     else:
          form=LoginForm()          
     return render(request,'myApp/login.html',{'form':form})     


def logoutView(request):
     logout(request)
     messages.success(request,"logged out successfully.")
     return redirect('home')