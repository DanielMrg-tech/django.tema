from django.urls import path
from . import views

urlpatterns = [
    path("ordered_names", views.ordered_names_view, name="ordered_names"),
    path("ordered_numbers", views.ordered_numbers_view, name="ordered_numbers"),
]