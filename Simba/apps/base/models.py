from django.db import models
from django_resized.forms import ResizedImageField
# Create your models here.
class Settings(models.Model):
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image_logo',
        verbose_name = 'Логотип'
    )


class Slide(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='slide_image',
        verbose_name='Фотография'
    )
    mini_description = models.CharField(
        max_length = 255,
        verbose_name = 'Мини описание '
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'  
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
