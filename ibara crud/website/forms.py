from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book,Genre





#Create Add Book Form

class DateInput(forms.DateInput):
    input_type = 'date'

class AddBookForm(forms.ModelForm):
  title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Book Title", "class": "form-control"}), label="")
  author = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Author Name", "class": "form-control"}), label="")
  publication_date = forms.DateField(required=True, widget=DateInput(attrs={"class": "form-control"}), label="")
  pages = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Number of Pages", "class": "form-control"}), label="")
  synopsis = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"Synopsis", "class": "form-control"}), label="")
  genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False, widget=forms.widgets.Select(attrs={"class": "form-control"}), label="")

  class Meta:
    model = Book
    fields = ['title', 'author', 'publication_date', 'pages', 'synopsis', 'genre']


class AddGenreForm(forms.ModelForm):
  name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Genre name", "class": "form-control"}), label="")
  description = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"desciription", "class": "form-control"}), label="")
  

  class Meta:
    model = Genre
    fields = ['name','description']


