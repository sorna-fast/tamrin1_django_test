# Generated by Django 5.0.6 on 2024-09-15 19:12

import apps.apiTestApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiTestApp', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/products/notphoto.png', upload_to=apps.apiTestApp.models.image_path),
        ),
    ]
