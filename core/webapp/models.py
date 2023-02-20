from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False, default='Title', verbose_name='Наименование')
    description = models.TextField(max_length=1800, null=True, blank=False, default='Description', verbose_name='Описание')
    category = models.ForeignKey(
        to='webapp.Category',
        on_delete=models.SET_NULL,
        default='Category',
        verbose_name='Категория',
        null=True,
        blank=False,
        related_name='category'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    price = models.DecimalField(max_digits=20, decimal_places=3, verbose_name='Стоимость')
    image = models.TextField(max_length=1000, null=False, blank=False, default='Image', verbose_name='Изоброжение')

    def __str__(self):
        return f'{self.title} {self.description} {self.category}'


class Category(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=1800, null=True, blank=False, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'
