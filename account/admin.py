from django.contrib import admin
from .models import Profile

admin.site.site_title = "admin site"
admin.site.site_header = "book store admin site"
admin.site.index_title = "book store admin site"
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "National_ID"]
    raw_id_fields = ["user"]
