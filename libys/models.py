from django.db import models

class Monufactures(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название Фирмы")

class Product(models.Model):
    title = models.CharField('Название Товара', max_length=135, db_index=True,)
    slug = models.SlugField('URL-адрес (slug)', unique=True, max_length=255,)
    sku = models.CharField('Артикул', unique=True, max_length=100,)
    category = models.ForeignKey("Категория", on_delete=models.PROTECT, related_name="products",)
