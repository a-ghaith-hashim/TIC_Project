# Generated by Django 4.2.10 on 2024-02-12 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0002_book_times_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=55),
            preserve_default=False,
        ),
    ]
