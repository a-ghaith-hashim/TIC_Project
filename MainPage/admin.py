from django.contrib import admin
from .models import *  # Importing all models from the current directory

# Registering models with the admin site
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(BookReview)

# Customizing the display of Transaction model in the admin site
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'dealing_type', 'quantity', 'price', 'rental_days','rental_price', 'total_price')

# Registering Transaction model with custom admin options
admin.site.register(Transaction, TransactionAdmin)
