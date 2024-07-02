from django import forms
# django provides built-in model that is User,contains-username,first_name,last_name,email,password etc.
from django.contrib.auth.models import User

# django provides built-in forms that is UserCreationForm form, contains- username ,password1 and password2
from django.contrib.auth.forms import UserCreationForm

# django provides built-in forms that is AuthenticationForm form, contains- username ,password
from django.contrib.auth.forms import AuthenticationForm

# creation of Registration Form inheriting UserCreationForm form and User model
class RegistrationForm(UserCreationForm):
     username=forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
     email=forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class':'form-control'}))
     password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
     password2=forms.CharField(label='confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
     class Meta:
          model=User
          fields=['username','email']

     def clean_email(self):
                 email = self.cleaned_data['email']
                 if User.objects.filter(email=email).exists():
                        raise forms.ValidationError("This email is already exist.")
                 return email


# class for loginForm
class LoginForm(AuthenticationForm):
       username=forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'})) 
       password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))