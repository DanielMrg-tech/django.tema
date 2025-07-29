from django.shortcuts import render

from django.http import HttpResponse

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

