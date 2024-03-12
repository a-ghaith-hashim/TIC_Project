from django import forms
from django.contrib.auth.models import User  # Importing User model from django.contrib.auth.models
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()  # Username field for login form
    password = forms.CharField(widget=forms.PasswordInput)  # Password field for login form

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)  # Password field for user registration
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)  # Password confirmation field for user registration

    class Meta:
        model = User  # Using Django's built-in User model for user registration
        fields = ["username", "first_name", "email"]  # Fields required for user registration

    def clean_password2(self):
        cd = self.cleaned_data

        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]  # Return the confirmed password

    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():  # Check if email already exists in the database
            raise forms.ValidationError("Email already exists.")
        return data  # Return cleaned email data

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User  # Using Django's built-in User model for user profile editing
        fields = ["first_name", "last_name", "email"]  # Fields editable in user profile

    def clean_email(self):
        data = self.cleaned_data["email"]
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)  # Exclude current user's email and check for duplicates
        if qs.exists():
            raise forms.ValidationError("Email already exists.")
        return data  # Return cleaned email data

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile  # Using custom Profile model for profile editing
        fields = ["date_of_birth", "National_ID", "ID_ImgOne", "ID_ImgTow"]  # Fields editable in profile
