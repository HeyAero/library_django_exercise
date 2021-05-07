from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def register(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message.success(req, f'Welcome, {username}!')
            return redirect('library-home')

# Create your views here.
