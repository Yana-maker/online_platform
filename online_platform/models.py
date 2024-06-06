from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class levels:
    """Модель уровней"""

    choices = (
        ("завод", 0),
        ("розничная сеть", 1),
        ("индивидуальный предприниматель", 2),
    )


class Product(models.Model):
    """Модель продукта"""

    title = models.TextField(max_length=150, verbose_name='название')
    model = models.TextField(unique=True, max_length=150, verbose_name='модель')
    release_data = models.DateTimeField(auto_now_add=True, verbose_name='дата выхода продукта на рынок')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Supplier(models.Model):
    """Модель поставщика"""

    title = models.TextField(max_length=150, verbose_name='название')
    level = models.CharField(choices=levels.choices, default=0, verbose_name='уровень')
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    country = models.TextField(max_length=150, verbose_name='страна')
    city = models.TextField(max_length=150, verbose_name='город')
    street = models.TextField(max_length=150, verbose_name='улица')
    house_number = models.TextField(max_length=150, verbose_name='номер дома')
    products = models.ManyToManyField(Product, verbose_name='продукты', db_index=True)
    debt = models.TextField(verbose_name='задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.title} - задолженность {self.debt}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
