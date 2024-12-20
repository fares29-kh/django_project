from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
path('authors/', views.AuthorListView.as_view(), name='Authors'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
path('bookinstance/<uuid:pk>/', views.BookInstanceDetailView.as_view(), name='bookinstance-detail'),
]
from django.urls import path
from .views import github_webhook

urlpatterns = [
    path('webhook/', github_webhook, name='github_webhook'),
]
