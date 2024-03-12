from django.contrib.auth.models import User  # Importing the User model from Django's built-in authentication system


class EmailAuthBackend:  # Custom authentication backend class
    def authenticate(self, request, username=None, password=None):  # Method to authenticate users
        try:
            user = User.objects.get(email=username)  # Retrieving user by email
            if user.check_password(password):  # Checking if the provided password is correct
                return user  # Returning the authenticated user
            return None  # Returning None if the password is incorrect
        except (User.DoesNotExist, User.MultipleObjectsReturned):  # Handling exceptions if user does not exist or multiple users are returned
            return None  # Returning None if user does not exist or multiple users are returned

    def get_user(self, user_id):  # Method to retrieve a user by their unique identifier
        try:
            return User.objects.get(pk=user_id)  # Retrieving user by primary key
        except User.DoesNotExist:  # Handling exception if user does not exist
            return None  # Returning None if user does not exist
