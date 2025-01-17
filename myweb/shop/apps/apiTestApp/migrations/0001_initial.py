# Generated by Django 5.0.6 on 2024-09-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('family', models.CharField(max_length=50, verbose_name='فامیلی')),
                ('email', models.EmailField(max_length=30, verbose_name='ایمیل')),
                ('age', models.PositiveIntegerField(verbose_name='سن')),
                ('username', models.CharField(max_length=50, verbose_name='نام کاربری')),
                ('password', models.CharField(max_length=60, verbose_name='پسورد')),
            ],
        ),
    ]
