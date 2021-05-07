# libary views file
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Author, Book

def not_found_404(req, exception):
  return render(req, 'public/404.html')

def home(req):
  book_data = { 'book_data': Book.objects.all()}
  return render(req, 'public/home.html', book_data)

@login_required
def show_book(req, id):
  book = get_object_or_404(Book, pk=id)
  book_data = { 'book': book }
  return render(req, 'public/books.html', book_data)