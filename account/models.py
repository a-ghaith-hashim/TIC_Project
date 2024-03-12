from django.db import models
from django.conf import settings

# Function to determine the upload path for user images
def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/users/user_<id>/<filename>
    return f"users/user_{instance.user.username}/{filename}"

# Model representing user profile information
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    National_ID = models.IntegerField(null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    ID_ImgOne = models.ImageField(upload_to=user_directory_path, blank=True)
    ID_ImgTow = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return f"{self.user.username}"
