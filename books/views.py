import json

from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpRequest
from rest_framework.templatetags.rest_framework import form_for_link

from books.models import Book
from rest_framework import viewsets
from books.serializers import BookSerializer
from books.forms import BookForm
from django.views.decorators.csrf import csrf_exempt
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

books_list = ["book 1", "Mockingbird", "Eminem: GReatest HITS", "Fahrenheit 471"]


@csrf_exempt
def books_view_simple(request: HttpRequest):
    if request.method == "GET":
        books_list.sort()
        context = {
            'books': books_list
        }
        return render(request, 'books2.html', context)



    if request.method == 'POST':
        data = json.loads(request.body)
        book_title = data["title"]
        books_list.append(book_title)
        return HttpResponse(" ")
@csrf_exempt
def books_view(request: HttpRequest):
    if request.method == "GET":
        context = {
            'form': BookForm()
        }
        return render(request, "create_book.html", context)
    elif request.method == "POST":
        form_with_data = BookForm(request.POST)
        if form_with_data.is_valid():
            form_with_data.save()
            return HttpResponse("Book Saved Succesfully!")
        else:
            return HttpResponse(form_with_data.errors)