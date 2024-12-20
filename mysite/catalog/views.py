from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance

def index(request):
    # Récupération des informations à afficher
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status='a').count()  # 'a' pour disponible
    num_authors = Author.objects.all().count()

    # Contexte des données à envoyer à la vue
    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
    }

    # Rendu de la page avec les données
    return render(request, 'index.html', context)

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 10
class AuthorListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Author
    paginate_by = 10
class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book

class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author
class BookInstanceDetailView(generic.DetailView):
    """Generic class-based detail view for a book instance."""
    model = BookInstance
