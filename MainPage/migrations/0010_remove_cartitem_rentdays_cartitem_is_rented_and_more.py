# Generated by Django 4.2.10 on 2024-03-01 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainPage', '0009_cartitem_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='rentdays',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='is_rented',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='rental_days',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
