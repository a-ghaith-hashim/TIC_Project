# Generated by Django 4.2.10 on 2024-03-01 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0007_cartitem_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='book',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
