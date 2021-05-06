# libary views file
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

book_data = { "book_data": [
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
  ]
}

def home(req):
  return render(req, 'public/home.html', book_data)

def show_book(req, id):
  return render(req, 'public/books.html', book_data["book_data"][id-1])