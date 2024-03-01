# Generated by Django 5.0.1 on 2024-01-03 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='image_logo', verbose_name='Логотип')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide_image', verbose_name='Фотография')),
                ('mini_description', models.CharField(max_length=255, verbose_name='Мини описание ')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]