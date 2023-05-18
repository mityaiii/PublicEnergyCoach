from django.contrib import admin

from . import models

admin.site.register(models.Meta)
admin.site.register(models.ContactForm)
