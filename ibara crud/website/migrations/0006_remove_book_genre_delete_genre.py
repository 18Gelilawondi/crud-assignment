# Generated by Django 5.0.1 on 2024-02-29 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_book_genre'),
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
