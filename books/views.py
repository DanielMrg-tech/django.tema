from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from books.models import Book
from rest_framework import viewsets
from books.serializers import BookSerializer

fruits = ['apple', 'banana', 'durian', 'pear']


names = [
    "Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana",
    "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai",
    "Diana", "Radu", "Laura", "Cristian", "Raluca",
    "Bianca",
]

numbers = [73, 28, 95, 14, 61, 39, 87, 5, 46, 32]

def ordered_names_view(request):
    sorted_names = sorted(names)
    return HttpResponse("<br>".join(sorted_names))

def ordered_numbers_view(request):
    sorted_numbers = sorted(numbers, reverse=True)
    return HttpResponse("<br>".join(map(str, sorted_numbers)))


def hello(request):
    return HttpResponse("Hello from our Books app")

def home(request):

    context = {
        'username': 'Alice',
        'logged_in': True,
        'current_time': datetime.now(),
        'fruits': fruits,
    }

    return render(request, 'Home.html', context)

def create_book(request):
    book1 = Book()
    book1.title = "Hello"
    book1.author = "Jack"
    book1.page_count = 35
    book1.save()
    return HttpResponse("Done")

def about(request):
    return render(request, 'about.html')

#aici legam cele doua clase adica avem GET POST si celelalte doua
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
