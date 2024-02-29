from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_date = models.DateField()
  pages = models.IntegerField()
  synopsis = models.TextField()
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

  def __str__(self) -> str:
    return self.title


 