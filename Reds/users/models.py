from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=17, verbose_name='Телефон')
    whatsapp = models.CharField(max_length=20, verbose_name='WhatsApp', help_text="Указать наличие")
    telegram = models.CharField(max_length=20, verbose_name='Telegram', help_text="Указать @ник")
    country = models.CharField(max_length=12, verbose_name='Страна')
    region = models.CharField(max_length=20, verbose_name='Регион, Область')
    city = models.CharField(max_length=12, verbose_name='Город')
    address = models.TextField(verbose_name='Почтовый адрес')
    category = models.CharField(max_length=12, verbose_name='Категория')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update
