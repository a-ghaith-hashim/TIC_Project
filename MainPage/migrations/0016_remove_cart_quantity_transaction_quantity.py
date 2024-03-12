# Generated by Django 4.2.10 on 2024-03-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0015_rename_retal_price_book_rental_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='transaction',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
