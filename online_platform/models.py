from django.db import models
from django.urls import reverse

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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'


class Contact(models.Model):
    """Модель контактов для сети"""

    email = models.EmailField(unique=True, verbose_name='электронная почта')
    country = models.TextField(max_length=150, verbose_name='страна')
    city = models.TextField(max_length=150, verbose_name='город')
    street = models.TextField(max_length=150, verbose_name='улица')
    house_number = models.TextField(max_length=150, verbose_name='номер дома')

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number},'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Network(models.Model):
    """Модель сети"""

    name = models.CharField(max_length=150, verbose_name="название", unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Поставщик")
    supplier_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                        verbose_name="задолженность перед поставщиком")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name="Контакты")

    def __str__(self):
        return f'{self.name} - задолженность {self.supplier_debt}'

    def get_absolute_url(self):
        return reverse('online_platform:supplier_retrieve', args=[str(self.supplier_id)])

    class Meta:
        verbose_name = 'сеть'
        verbose_name_plural = 'сети'
