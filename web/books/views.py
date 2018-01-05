from django.shortcuts import render, redirect
from .models import Member, Books
 
def index(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'books/index.html', context)
 
def create(request):
    book = Books(book_title=request.POST['book_title'], writer=request.POST['witer'], 
                synopsis=request.POST['synopsis'], publisher=request.POST['publisher'], 
                publish_date=request.POST['publish_date'])
    book.save()
    return redirect('/')

def add_book(request):
    # members = Member.objects.all()
    # context = {'members': members}
    return render(request, 'books/add_book.html', {})

 
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'books/edit.html', context)
 
def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/books/')
 
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/books/')