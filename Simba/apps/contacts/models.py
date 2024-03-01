from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=25, verbose_name = "Заголовок")
    description1 = models.CharField(max_length=255, verbose_name = "Мини описание")
    description2 = models.CharField(max_length=255, verbose_name = "Описание")
    phone_number = models.CharField(max_length=15, verbose_name = "Телефонный номер")
    whatsapp = models.CharField(max_length=15, verbose_name = "Ватсап")
    inst = models.URLField(verbose_name = "инстаграм")
    email = models.EmailField(verbose_name = "Электронная почта")
    address = models.CharField(max_length=100, verbose_name = "Адрес")

    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    