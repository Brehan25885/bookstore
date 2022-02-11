from turtle import title
from urllib import response
from django.test import TestCase
from django.urls  import reverse
from .models import Book

# Create your tests here.

class BookTest(TestCase):
    def setUp(self) -> None:
        self.book =Book.objects.create(title='Harry Pooter',author='Jk Rowling',price='24')
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}','Harry Pooter')
        self.assertEqual(f'{self.book.author}','Jk Rowling')
        self.assertEqual(f'{self.book.price}','24')
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Harry Pooter')
        self.assertTemplateUsed(response,'books/book_list.html')
    def test_book_details_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response= self.client.get('/books/1234')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'Harry Pooter')
        self.assertTemplateUsed(response,'books/book_detail.html')

