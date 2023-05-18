from django.db import models
from django.utils import timezone


class Meta(models.Model):
    key = models.TextField(unique=True, verbose_name="Ключ (ссылка)")
    title = models.TextField(verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Мета"
        verbose_name_plural = "Мета"

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    first_name = models.TextField(verbose_name="Имя")
    second_name = models.TextField(verbose_name="Фамилия")
    email = models.TextField(verbose_name="Почта")
    phone_number = models.TextField(verbose_name="Контактный номер")
    telegram = models.TextField(verbose_name="Телеграм", null=True, blank=True)
    message = models.TextField(verbose_name="Сообщение")
    contact_date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ['contact_date']
        verbose_name = "Контактная Форма"

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.contact_date}'
