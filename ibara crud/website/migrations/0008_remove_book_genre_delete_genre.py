# Generated by Django 5.0.1 on 2024-02-29 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_genre_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
