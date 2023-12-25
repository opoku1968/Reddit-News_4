# Generated by Django 3.2.23 on 2023-12-07 16:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogforum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='pro_pic.png', max_length=255, null=True, verbose_name='profile_pic'),
        ),
    ]