from MainPage.models import Book


def global_variables(request):
    return {"allbook": Book.objects.all()}
