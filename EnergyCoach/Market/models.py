from django.core.validators import MinValueValidator
from django.db import models

from ckeditor.fields import RichTextField


class MarketProductTag(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=50)

    class Meta:
        verbose_name = 'Категория Товара'
        verbose_name_plural = 'Категории Товаров'

    def __str__(self):
        return self.title


class MarketProduct(models.Model):
    title =  models.CharField(max_length=1000, verbose_name="Название")
    price = models.DecimalField(validators=[MinValueValidator(1)], max_digits=10, decimal_places=2, verbose_name="Цена")
    tags = models.ManyToManyField(MarketProductTag, blank=True, null=True, related_name="MarketTag", verbose_name="Категории")
    image = models.ImageField(verbose_name="Картинка")
    content = RichTextField(verbose_name="Контент")
    subcontent = RichTextField(verbose_name="Дополнительный контент")
    publication_date = models.DateTimeField(verbose_name="Дата публикации")
    status = models.BooleanField(verbose_name="Опубликовать")

    class Meta:
        ordering = ['publication_date']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
