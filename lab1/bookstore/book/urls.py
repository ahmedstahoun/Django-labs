from django.urls import path
from .views import index, library_list , book_detail , book_delete , book_update , book_create ,book_add


app_name = 'book'

urlpatterns = [
    path('index', index, name='book-index'),
    path('library_list/', library_list, name="library-list"),
    path('book_detail/<int:book_id>', book_detail, name="book-detail"),
    path('book_delete/<int:book_id>', book_delete, name="book-delete"),
    path('book_update/<int:book_id>', book_update, name="book-update"),
    path('book_create/', book_create, name="book-create"),
    path('book_add/', book_add , name="book-add"),
]
