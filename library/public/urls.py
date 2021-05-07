from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='public-home'),
    path('books/<int:id>', views.show_book, name='public-books'),
    path('books/new', views.create_book, name='public-create'),
]