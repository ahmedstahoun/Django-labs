from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    print("hello")
    print(request.body)
    return render(request, 'main/base_layout.html')


books_list = [
    {
        
        'id': 1,
        'name': 'book-1',
        'author': 1,
        'description': "Learning about html and css",
    },
    {
        
        'id': 2,
        'name': 'book-2',
        'author': 4,
        'description': "Learning Python ",
    },
    {
        
        'id': 3,
        'name': 'book-3',
        'author': 2,
        'description': "LearningJs ",
    },
]


def library_list(request):
    my_context = {'books_list': books_list}
    # template_loader > book/templates/
    return render(request, 'book/book_list.html', context=my_context)

def _get_book(book_id):
    for book in books_list:
        if 'id' in book and book['id'] == book_id:
            return book
    return None

def book_detail(request, *args, **kwrgs):
    book_id = kwrgs.get('book_id')
    book_object = _get_book(book_id)
    if book_object:
        my_context = {
            'book_id': book_object.get('id'),
            'book_name': book_object.get('name'),
            'book_author': book_object.get('author'),
            'book_description': book_object.get('description')
        }
        return render(request, 'book/book_details.html', context=my_context)
    else:
        return render(request , 'book/book_list.html')
    
def book_delete(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    if books_list:
        books_list.remove(book_object)
    return redirect('book:library-list') 

def book_update(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    for book in books_list:
        if book == book_object:
            book['name'] = f"Update {book_object['name']}"
            
    return redirect('book:library-list') 

def book_create(request):
    return render(request,'book/book_create.html')

def book_add(request):
    if request.method == 'POST':
        my_context = {
            'id': request.POST['id'],
            'name': request.POST['name'],
            'author': request.POST['author'],
            'description': request.POST['description']
        }
        books_list.append(my_context)
    all_books = {'books_list': books_list}
    return render(request, 'book/book_list.html', context=all_books)
