from django.urls import path
from .views import index , book_details, delete_book, update_book, create_book, add_book

app_name = 'book'

# http://localhost:8000/post/2/comment/1
urlpatterns = [
    path('index', index, name='book-index'),
    path('create_book',create_book,name="book-create"),
    path('add_new_book',add_book,name="book-add"),
    path('book_details/<int:pk>', book_details, name="book-detail"),
    path('delete_book/<int:pk>', delete_book, name="book-delete"),
    path('update_book/<int:pk>', update_book, name="book-update"),
]
