# Generated by Django 5.0 on 2023-12-15 21:35

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_photo_profile_id_imgone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ID_ImgOne',
            field=models.ImageField(blank=True, upload_to=account.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ID_ImgTow',
            field=models.ImageField(blank=True, upload_to=account.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='National_ID',
            field=models.IntegerField(null=True),
        ),
    ]
