from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField
# Create your models here.

class Style(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    descriptions = RichTextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'

class StyleInfo(models.Model):
    place_info = models.ForeignKey(Style,related_name = "place_info", on_delete  = models.CASCADE )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='price/',
        verbose_name="фотография",
        blank = True, null = True
    )

    class Meta:
        unique_together = ('place_info', 'image')

class Glance(models.Model):
    name = models.CharField(
        max_length =255,
        verbose_name = 'Название',
        blank=True, null= True
    )
    descriptions = RichTextField(
        verbose_name = 'Описание',
        blank=True, null= True
    )
    image1 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='price/',
        verbose_name = 'Фотография сверху',
        blank=True, null= True
    )
    title1 = models.CharField(
        max_length = 255,
        verbose_name = "Название",
        blank=True, null= True
    )
    image2 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='price/',
        verbose_name = 'Фотография сверху',
        blank=True, null= True
    )
    title2 = models.CharField(
        max_length = 255,
        verbose_name = "Название",
        blank=True, null= True
    )
    image3 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name = 'Фотография сверху',
        blank=True, null= True
    )
    title3 = models.CharField(
        max_length = 255,
        verbose_name = "Название",
        blank=True, null= True
    )
    image4 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name = 'Фотография сверху',
        blank=True, null= True
    )
    title4 = models.CharField(
        max_length = 255,
        verbose_name = "Название",
        blank=True, null= True
    )
    image5 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name = 'Фотография сверху',
        blank=True, null= True
    )
    title5 = models.CharField(
        max_length = 255,
        verbose_name = "Название",
        blank=True, null= True
    )
    


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория взгляда'
        verbose_name_plural = 'Категории взгляда'



class Discount(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        
        upload_to='image_goods',
        verbose_name='Фотография'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    descriptions = RichTextField(
        verbose_name = 'Описание'
    )
    now_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена сейчас'
    )
    before_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена раньше'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Collection(models.Model):
    descriptions =RichTextField(
        verbose_name = 'Описание'
    )
    
    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class CollectionInline(models.Model):
    place_info = models.ForeignKey(Collection,related_name = "collection_info", on_delete  = models.CASCADE )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='up_photo/',
        verbose_name = 'Фотография сверху',
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена'
    )
    size = models.CharField(
        max_length = 255,
        verbose_name = 'Размеры'
    )
    def __str__(self):
        return self.title
    class Meta:
        unique_together = ('place_info', 'image')

class Testimonials(models.Model):
    mini_descriptions = RichTextField(
        max_length =255,
        verbose_name = 'Мини описание'
    )
    def __str__(self):
        return self.mini_descriptions
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = 'Отзывы'
    

class TestimonialsInline(models.Model):
    place_info = models.ForeignKey(Testimonials,related_name = "testimonials_info", on_delete  = models.CASCADE )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='testimonials/image',
        verbose_name='Фото клиентов'
    )
    testimonial = RichTextField(
        verbose_name = 'Отзыв'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя клиента'
    )
    def __str__(self):
        return self.name
    class Meta:
        unique_together = ('place_info', 'image')
    
class Trends(models.Model):
    first_descrip = RichTextField(
        verbose_name = 'Главное описание'
    )
    image =ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='trends_image/',
        verbose_name='Большое фото'
    )
    goods = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='goods/trend/image',
        verbose_name='Фото товара'
    )
    card_image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='card_image/',
        verbose_name='Фото внутри карточки'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название товара'
    )
    descriptions =RichTextField(
        verbose_name = 'Описание товара'
    )
    now_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена сейчас'
    )
    before_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена раньше'
    )
    size = models.CharField(
        max_length = 255,
        verbose_name = 'Размеры'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тренд'
        verbose_name_plural = 'Тренды'
   
    
class About(models.Model):
    title = models.CharField(
        max_length = 100, 
        verbose_name = "название"
    )
    description = models.CharField(
        max_length=155, 
        verbose_name = "описание"
    )
    mini_description = models.CharField(
        max_length=155, 
        verbose_name = "мини описание"
    )
    text1 =RichTextField( 
        verbose_name = "первый текст"
    )
    text2 =RichTextField( 
        verbose_name = "второй текст"
    )
    image1 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="image/", 
        verbose_name="фото"
    )
    image2 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="image/", 
        verbose_name="фото"
    )
    image3 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="image/", 
        verbose_name="фото"
    )
    image4 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="image/", 
        verbose_name="фото"
    )
    image5 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="image/", 
        verbose_name="фото"
    )
    image6 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="image/", 
        verbose_name="фото"
    )
    image7 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="image/", 
        verbose_name="фото"
    )
    image8 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="image/", 
        verbose_name="фото"
    )
    image9 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="image/", 
        verbose_name="фото"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class Faqs(models.Model):
    title = models.CharField(
        max_length = 100, 
        verbose_name = "название"
    )
    description = models.CharField(
        max_length=155, 
        verbose_name = "описание"
    )
    question = models.CharField(
        max_length = 155, 
        verbose_name = "Вопрос"
    )
    answer =RichTextField(
        verbose_name = "Ответ"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
    
   

class Partner(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='partner_image/',
        verbose_name='Фотография '
    )
    class Meta:
        verbose_name = 'Парнер'
        verbose_name_plural ='Партнеры'


class Art(models.Model):
    part = models.CharField(
        max_length = 255,
        verbose_name = 'Название части'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    descriptions =RichTextField(
        verbose_name = 'Описание товара'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отдел товаров'
        verbose_name_plural = 'Отделы товаров'


class ClothesColor(models.Model):
    image1 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='color_image1/',
        verbose_name='Фото для рассветки 1 ',
        blank=True, null=True
    )
    image2 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='color_image2/',
        verbose_name='Фото  для рассветки 2',
        blank=True, null=True
    )
    image3 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='color_image3/',
        verbose_name='Фото  для рассветки 3',
        blank=True, null=True
    )
    title= models.CharField(
        max_length = 255,
        verbose_name = 'Название товара'
    )
    descriptions =RichTextField(
        verbose_name = 'Описание'
    )
    now_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена сейчас'
    )
    before_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена раньше'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Одежды с рассветкой'
        verbose_name_plural = 'Одежды с рассветками'

class News(models.Model):
    descriptions =RichTextField(
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = 'Последняя новость'
        verbose_name_plural = 'Последнии новости'


class NewsInline(models.Model):
    place_info = models.ForeignKey(News,related_name = "lastnews_info", on_delete  = models.CASCADE )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='news_image/',
        verbose_name='Фотография'
    )
    mini_descriptions =RichTextField(
        max_length =255,  
        verbose_name = 'Мини описание'
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        blank = True,null = True
    )
    class Meta:
        unique_together = ('place_info', 'image')


    

    