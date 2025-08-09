from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet

#aici trebuie sa cream un router si sa il legam de register

router = DefaultRouter()
router.register('books', BookViewSet, basename='book_viewset')

urlpatterns = [
    path("ordered_names/", views.ordered_names_view, name="ordered_names"),
    path("ordered_numbers/", views.ordered_numbers_view, name="ordered_numbers"),
    path("hello/", views.hello, name="hello"),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create_book/', views.create_book, name='create_book'),
    path('api/', include(router.urls))
]