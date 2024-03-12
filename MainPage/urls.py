from django.urls import path  # Importing necessary function from Django
from . import views  # Importing views module from the current directory

urlpatterns = [  # List of URL patterns for routing
    path("", views.homePage, name="homePage"),  # Route for the home page
    path("books/", views.books, name="books"),  # Route for the books page
    path("about/", views.about, name="about"),  # Route for the about page
    path("book_detail/<int:id>", views.book_detail, name="book_detail"),  # Route for individual book detail
    path("review/", views.review_rate, name="review"),  # Route for submitting reviews
    path("add_transaction/", views.add_transaction, name="add_transaction"),  # Route for adding transactions
    path("checkout_cart/", views.checkout_cart, name="checkout_cart"),  # Route for checking out the cart
    path("cart/", views.cart_view, name="cart"),  # Route for viewing the cart
]
