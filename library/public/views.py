# libary views file
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import NewBookForm, BorrowBookForm, UnborrowBookForm

from .models import Author, Book

def not_found_404(req, exception):
  return render(req, 'public/404.html')

def home(req):
  book_data = { 'book_data': Book.objects.all()}
  return render(req, 'public/home.html', book_data)

@login_required
def show_book(req, id):
  book = get_object_or_404(Book, pk=id)
  if req.method == 'POST':
    form = BorrowBookForm(req.POST)
    form2 = UnborrowBookForm(req.POST)
    if book.borrower == req.user:
      if form2.is_valid():
        print('Test2')
        book.borrower = None
        book.save()
        return redirect('public-books', id=id)
    else:
      if form.is_valid():
        print('Test1')
        book.borrower = req.user
        book.save()
        return redirect('public-books', id=id)
    
  else:
    form = BorrowBookForm(initial={'borrower': req.user})
    form2 = UnborrowBookForm(initial={'borrower': req.user})
  book_data = { 
              'book': book, 
              'form': form,
              'form2': form2
              }
  return render(req, 'public/books.html', book_data)
  

@login_required
def create_book(req):
  if req.method == 'POST':
    book = NewBookForm(req.POST)
    if book.is_valid():
      id = book.save().id
      return redirect('public-books', id=id)
  else:
    form = NewBookForm()
    data = {'form': form}
    return render(req, 'public/new.html', data)