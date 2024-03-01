# Generated by Django 5.0.1 on 2024-01-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_rename_image_about_image1_about_image2_about_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='glance',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Фотография сверху'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='glance',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='GlanceInfo',
        ),
    ]
