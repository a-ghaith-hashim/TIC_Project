# Generated by Django 4.2.10 on 2024-03-06 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0014_remove_book_high_rate_remove_book_retal_period_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='retal_price',
            new_name='rental_price',
        ),
    ]
