from django.db import models  # Importing Django's models module
from account.models import Profile  # Importing Profile model from account app
from django.db.models import DecimalField  # Importing DecimalField from Django's models


class Category(models.Model):  # Defining Category model
    name = models.CharField(max_length=50)  # Field for category name
    description = models.TextField()  # Field for category description

    def __str__(self):  # String representation of the Category object
        return self.name  # Returning the category name as string


class Book(models.Model):  # Defining Book model
    category = models.ForeignKey(  # Relationship with Category model
        Category, on_delete=models.PROTECT, null=True, blank=True
    )
    status_choices = [  # Choices for book status
        ("availble", "availble"),
        ("rental", "rental"),
        ("sold", "sold")
    ]
    title = models.CharField(max_length=250)  # Field for book title
    author = models.CharField(max_length=50)  # Field for book author
    photo_book = models.ImageField(upload_to="img/book/%y/%m/%d", null=True, blank=True)  # Field for book photo
    description = models.TextField()  # Field for book description
    page = models.IntegerField(null=True, blank=True)  # Field for number of pages
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Field for book price
    rental_price = models.DecimalField(  # Field for rental price
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    active = models.BooleanField(default=True)  # Field for book activity status
    status = models.CharField(  # Field for book status
        max_length=50, choices=status_choices, null=True, blank=True
    )

    def __str__(self):  # String representation of the Book object
        return self.title  # Returning the book title as string


class Transaction(models.Model):  # Defining Transaction model
    dealing_type_choices = [  # Choices for dealing type
        ("buy", "buy"),
        ("rent", "rent")
    ]
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)  # Relationship with User profile
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Relationship with Book
    dealing_type = models.CharField(max_length=50, choices=dealing_type_choices)  # Field for dealing type
    rental_days = models.PositiveIntegerField(default=0)  # Field for rental days
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Field for price
    rental_price = models.DecimalField(max_digits=5, decimal_places=2)  # Field for rental price
    quantity = models.PositiveIntegerField(default=1)  # Field for quantity
    rental_fee = models.DecimalField(  # Field for rental fee
        max_digits=5, decimal_places=2, null=True, blank=True
    )  # Calculated based on rental_days and rental_price

    @property
    def total_price(self):  # Property for total price
        if self.dealing_type == 'buy':  # If dealing type is buying
            return self.price * self.quantity  # Calculate total price for buying
        elif self.dealing_type == 'rent':  # If dealing type is renting
            if self.rental_fee:  # Avoid division by zero if rental_fee is not set
                return self.rental_fee * self.quantity  # Calculate total price for renting
            else:
                return None  # Indicate missing data
        else:
            raise ValueError("Invalid dealing_type: {}".format(self.dealing_type))  # Raise error for invalid dealing type

    def __str__(self):  # String representation of the Transaction object
        return f"{self.dealing_type} - {self.book.title}- {self.quantity}x"  # Returning formatted string


class Cart(models.Model):  # Defining Cart model
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)  # Relationship with User profile
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)  # Relationship with Transaction

    def __str__(self):  # String representation of the Cart object
        return f"{self.user}'s cart - {self.transaction.book.title}"  # Returning formatted string


class BookReview(models.Model):  # Defining BookReview model
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)  # Relationship with User profile
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Relationship with Book
    comment = models.TextField(null=True, blank=True)  # Field for review comment
    rate = models.IntegerField(default=0)  # Field for review rating
    created = models.DateTimeField(auto_now_add=True)  # Field
