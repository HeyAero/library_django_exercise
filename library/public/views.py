# libary views file
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

def home(req):
  return render(req, 'public/home.html')

def show_book(req):
  return render(req, 'public/books.html')