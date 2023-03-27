from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='сотрудник', on_delete=models.SET_NULL,
                             **NULLABLE,editable=False)
    email = models.EmailField()
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=80, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=80, verbose_name='Улица', **NULLABLE)
    house_number = models.PositiveIntegerField(**NULLABLE)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='сотрудник', on_delete=models.SET_NULL,
                             **NULLABLE,editable=False)
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель', **NULLABLE)
    date = models.DateField(verbose_name='Дата выхода')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Supplier(models.Model):
    FACTORY = 'FACTORY'
    RETAIL = 'RETAIL'
    INDIVIDUAL = 'INDIVIDUAL'

    EMPLOYEE_TYPES = (
        (FACTORY, 'Завод'),
        (RETAIL, 'Розничная сеть'),
        (INDIVIDUAL, 'Индивидуальный предприниматель'))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='сотрудник', on_delete=models.SET_NULL,
                             **NULLABLE, editable=False)
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    name = models.CharField(max_length=100, verbose_name='Название сети')
    contact = models.ForeignKey('electronics.Contact', on_delete=models.SET_NULL, verbose_name='Контакты', related_name='contact',**NULLABLE)
    product = models.ForeignKey('electronics.Product', on_delete=models.SET_NULL, verbose_name='Продукты', related_name='product',**NULLABLE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='Задолженность',**NULLABLE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name
