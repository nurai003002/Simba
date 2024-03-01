# Generated by Django 5.0.1 on 2024-01-03 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.CharField(max_length=155, verbose_name='описание')),
                ('image', models.ImageField(upload_to='image/', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(max_length=255, verbose_name='Название части')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('descriptions', models.TextField(verbose_name='Описание товара')),
            ],
            options={
                'verbose_name': 'Отдел товаров',
                'verbose_name_plural': 'Отделы товаров',
            },
        ),
        migrations.CreateModel(
            name='ClothesColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='color_image1/', verbose_name='Фото для рассветки 1 ')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='color_image2/', verbose_name='Фото  для рассветки 2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='color_image3/', verbose_name='Фото  для рассветки 3')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('now_price', models.CharField(max_length=255, verbose_name='Цена сейчас')),
                ('before_price', models.CharField(max_length=255, verbose_name='Цена раньше')),
            ],
            options={
                'verbose_name': 'Одежды с рассветкой',
                'verbose_name_plural': 'Одежды с рассветками',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_goods', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('now_price', models.CharField(max_length=255, verbose_name='Цена сейчас')),
                ('before_price', models.CharField(max_length=255, verbose_name='Цена раньше')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.CharField(max_length=155, verbose_name='описание')),
                ('question', models.CharField(max_length=155, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Glance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория взгляда',
                'verbose_name_plural': 'Категории взгляда',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Последняя новость',
                'verbose_name_plural': 'Последнии новости',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partner_image/', verbose_name='Фотография ')),
            ],
            options={
                'verbose_name': 'Парнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Стиль',
                'verbose_name_plural': 'Стили',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mini_descriptions', models.TextField(max_length=255, verbose_name='Мини описание')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Trends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_descrip', models.TextField(verbose_name='Главное описание')),
                ('image', models.ImageField(upload_to='trends_image/', verbose_name='Большое фото')),
                ('goods', models.ImageField(upload_to='goods/trend/image', verbose_name='Фото товара')),
                ('card_image', models.ImageField(upload_to='card_image/', verbose_name='Фото внутри карточки')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('descriptions', models.TextField(verbose_name='Описание товара')),
                ('now_price', models.CharField(max_length=255, verbose_name='Цена сейчас')),
                ('before_price', models.CharField(max_length=255, verbose_name='Цена раньше')),
                ('size', models.CharField(max_length=255, verbose_name='Размеры')),
            ],
            options={
                'verbose_name': 'Тренд',
                'verbose_name_plural': 'Тренды',
            },
        ),
        migrations.CreateModel(
            name='CollectionInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография сверху')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размеры')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_info', to='secondary.collection')),
            ],
            options={
                'unique_together': {('place_info', 'image')},
            },
        ),
        migrations.CreateModel(
            name='GlanceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография сверху')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glance_info', to='secondary.glance')),
            ],
            options={
                'unique_together': {('place_info', 'image')},
            },
        ),
        migrations.CreateModel(
            name='NewsInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_image/', verbose_name='Фотография')),
                ('mini_descriptions', models.TextField(max_length=255, verbose_name='Мини описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lastnews_info', to='secondary.news')),
            ],
            options={
                'unique_together': {('place_info', 'image')},
            },
        ),
        migrations.CreateModel(
            name='StyleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_info', to='secondary.style')),
            ],
            options={
                'unique_together': {('place_info', 'image')},
            },
        ),
        migrations.CreateModel(
            name='TestimonialsInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonials/image', verbose_name='Фото клиентов')),
                ('testimonial', models.TextField(verbose_name='Отзыв')),
                ('name', models.CharField(max_length=255, verbose_name='Имя клиента')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials_info', to='secondary.testimonials')),
            ],
            options={
                'unique_together': {('place_info', 'image')},
            },
        ),
    ]