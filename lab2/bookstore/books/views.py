from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Books
from .forms import BooksForm
# Create your views here.


def index(request):
    print("hello")
    print(request.body)
    all_books = Books.objects.all()
    return render(request, 'book/book_list.html', context={"books": all_books})


# books_list = [
#     {
        
#         'id': 1,
#         'name': 'book-1',
#         'author': 1,
#         'description': "Learning about html and css",
#     },
#     {
        
#         'id': 2,
#         'name': 'book-2',
#         'author': 4,
#         'description': "Learning Python ",
#     },
#     {
        
#         'id': 3,
#         'name': 'book-3',
#         'author': 2,
#         'description': "LearningJs ",
#     },
# ]


def library_list(request):
    my_context = {'books_list': books_list}
    # template_loader > book/templates/
    return render(request, 'book/book_list.html', context=my_context)

def _get_book(book_id):
    for book in books_list:
        if 'id' in book and book['id'] == book_id:
            return book
    return None

def create_book(request):
    return render(request, 'book/book_create.html')

def book_details(request, pk):
    book= Books.objects.get(pk=pk)
    return render(request ,'book/book_details.html',context={"book":book})
    
def delete_book(request, pk):
    Books.objects.get(pk=pk).delete()
    return redirect("book:book-index")

def update_book(request, pk):
    book=Books.objects.get(pk=pk)
    form=BooksForm(instance=book)
    if request.method == "POST":
        form= BooksForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()      
            return redirect('book:book-detail',pk=book.id)
            # return render(request, 'book:book-detail',pk=book.id)
    return render(request, 'book/book_edit.html', context={
        'form': form, 
        'book': book
    })


def add_book(request):
    form = BooksForm()
    if request.method == 'POST':
        form= BooksForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("book:book-index")
    return render(request, 'book/book_create.html', context={
        'form':form
    })
