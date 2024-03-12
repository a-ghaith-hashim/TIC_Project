# Generated by Django 4.2.10 on 2024-03-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0016_remove_cart_quantity_transaction_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='rental_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
