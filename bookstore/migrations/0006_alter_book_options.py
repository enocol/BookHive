# Generated by Django 5.2 on 2025-05-05 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_book_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
    ]
