from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


@login_required
def dashboard(request):
    # Renders the dashboard template with the current user's section
    return render(request, "account/dashboard.html", {"section": "dashboard"})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user based on the form data
            new_user = user_form.save(commit=False)
            # Set the user's password using the form data
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            # Create a corresponding profile for the new user
            Profile.objects.create(user=new_user)
            # Render the registration success template with the new user's information
            return render(request, "account/register_done.html", {"new_user": new_user})
    else:
        # If not a POST request, create a blank user registration form
        user_form = UserRegistrationForm()
    # Render the registration form template with the user registration form
    return render(request, "account/register.html", {"user_form": user_form})


@login_required
def edit(request):
    if request.method == "POST":
        # If it's a POST request, populate user and profile forms with submitted data
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            # If both forms are valid, save the user and profile forms
            user_form.save()
            profile_form.save()
            # Display a success message
            messages.success(request, "Profile has been updated successfully.")
        else:
            # Display an error message if either form is invalid
            messages.error(request, "Error updating your profile.")

    else:
        # If not a POST request, create blank user and profile forms
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    # Render the edit profile template with user and profile forms
    return render(
        request,
        "account/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
