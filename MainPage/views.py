from collections import UserDict  # Importing necessary modules
from django.shortcuts import get_object_or_404, redirect, render  # Importing necessary modules
from .models import *  # Importing all models from the current app

# View for rendering the home page
def homePage(request):
    allBooks = Book.objects.filter(active=True)
    return render(request, "templates/home.html", {"allBooks": allBooks})

# View for rendering the books page
def books(request):
    allBooks = Book.objects.filter(active=True)
    return render(request, "templates/books.html", {"allBooks": allBooks})

# View for rendering the about page
def about(request):
    return render(request, "templates/about.html")

# View for rendering details of a book
def book_detail(request, id):
    details = get_object_or_404(Book, id=id)
    reviews = BookReview.objects.filter(book=details)
    return render(
        request, "templates/book_detail.html", {"details": details, "reviews": reviews}
    )

# View for adding a transaction (buy/rent) for a book
def add_transaction(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        price = request.POST.get("book_price")
        rental_price = request.POST.get('rental_price')
        user = request.user
        book = Book.objects.get(pk=book_id)
        rental_days = int(request.POST.get("rental_days"))  # Convert to integer
        dealing_type = request.POST.get("dealing_type")
        # Calculate rental fee only if dealing type is rent
        rental_fee = None
        if dealing_type == "rent":
            rental_fee = book.rental_price * rental_days
        transaction = Transaction(
            user=user.profile,
            book=book,
            rental_days=rental_days,
            dealing_type=dealing_type,
            price=price,
            rental_price= rental_price,
            rental_fee=rental_fee,  # Set rental_fee if calculated
            quantity = 1
        )
        transaction.save()
        return redirect(cart_view)

# View for updating cart items during checkout
def checkout_cart(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('quantity_'):  
                item_id = key.split('_')[1] 
                quantity = int(value) 
                
                cart_item = Transaction.objects.get(pk=item_id)
                cart_item.quantity = quantity
                cart_item.save()
        return redirect(cart_view)

# View for rendering the cart page
def cart_view(request):
    cart_items = None
    if request.user.is_authenticated:
        cart_items = Transaction.objects.filter(user=request.user.profile)
    return render(request, "templates/cart.html", {"cart_items": cart_items})

# View for adding a review and rating for a book
def review_rate(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = get_object_or_404(Book, id=book_id)
        comment = request.POST.get("comment")
        rate = request.POST.get("rate")
        user = request.user
        book_review = BookReview(
            user=user.profile, book=book, comment=comment, rate=rate
        )
        book_review.save()

        return redirect("book_detail", id=book_id)
