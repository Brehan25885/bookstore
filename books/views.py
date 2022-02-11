from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Book
# Create your views here.

class BookListView(ListView):
    model=Book
    context_object_name = 'book_list'
    template_name='books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name='books/book_detail.html'