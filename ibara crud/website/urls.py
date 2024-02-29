
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('book_record/<int:pk>',views.book_record,name='book_rec'),
    path('genre_record/<int:pk>',views.genre_record,name='genre_rec'),
    path('delete_record/<int:pk>',views.delete_book_record,name='delete_book_record'),
    path('delete_genre/<int:pk>',views.delete_genre,name='delete_genre'),
    path('add_book/',views.add_book,name='add_book'),
    path('add_genre/',views.add_genre,name='add_genre'),
     path('update_book_record/<int:pk>',views.update_book_record,name='update_book'),
     path('update_genre/<int:pk>',views.update_genre,name='update_genre'),
    
    
]