from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import AddBookForm,AddGenreForm
from.models import *
# Create your views here.

def home(request):
  Books = Book.objects.all()
  Genres = Genre.objects.all()
  return render(request,'home.html',{'book':Books,'genre':Genres})


def book_record(request,pk):
  book_record = Book.objects.get(id=pk)
  return render(request,'record.html',{'book_record':book_record})

def genre_record(request,pk):
  genre_record = Genre.objects.get(id=pk)
  return render(request,'genre.html',{'genre_record':genre_record})


def delete_book_record(request,pk):
  delete_book = Book.objects.get(id=pk)
  delete_book.delete()
  messages.success(request,'Book deleted successfully')
  return redirect('home')

def delete_genre(request,pk):
  delete_genre = Genre.objects.get(id=pk)
  delete_genre.delete()
  messages.success(request,'Book deleted successfully')
  return redirect('home')

  
def add_book(request):
  form = AddBookForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      add_book = form.save()
      messages.success(request,"Book added")
      return redirect('home')     
  return render(request,'addbook.html',{"form":form})

def add_genre(request):
  form = AddGenreForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      add_genre = form.save()
      messages.success(request,"genre added")
      return redirect('home')     
  return render(request,'addgenre.html',{"form":form})

    
def update_book_record(request,pk):
  current_book = Book.objects.get(id=pk)
  form = AddBookForm(request.POST or None,instance=current_book)
  if form.is_valid():
    form.save()
    messages.success(request,"Book Detail has been updated")
    return redirect('home') 
  return render(request,'updatebook.html',{"form":form})

def update_genre(request,pk):
  current_genre = Genre.objects.get(id=pk)
  form = AddGenreForm(request.POST or None,instance=current_genre)
  if form.is_valid():
    form.save()
    messages.success(request,"Genre Detail has been updated")
    return redirect('home') 
  return render(request,'updatgenre.html',{"form":form})
