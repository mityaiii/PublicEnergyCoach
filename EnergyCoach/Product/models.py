from django.db import models

from ckeditor.fields import RichTextField


class ProductTag(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=50)

    class Meta:
        verbose_name = 'Категория Услуг'
        verbose_name_plural = 'Категории Услуг'

    def __str__(self):
        return self.title



class Product(models.Model):
    title =  models.CharField(max_length=1000, verbose_name="Название")
    tags = models.ManyToManyField(ProductTag, blank=True, null=True, related_name="ProductTag", verbose_name="Категории")
    image = models.ImageField(verbose_name="Картинка")
    content = RichTextField(verbose_name="Контент")
    subcontent = RichTextField(verbose_name="Дополнительный контент")
    publication_date = models.DateTimeField(verbose_name="Дата публикации")
    status = models.BooleanField(verbose_name="Опубликовать")

    class Meta:
        ordering = ['publication_date']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title
