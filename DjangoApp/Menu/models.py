from django.db import models


class CategoryMenu(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категория меню")

    class Meta:
        verbose_name = 'Неотображаемое название меню'
        verbose_name_plural = 'Неотображаемое название меню'


class MenuBar(models.Model):
    title = models.CharField(max_length=50, verbose_name="Пункт меню")
    url = models.SlugField(unique=True, verbose_name="URL адрес")
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE, verbose_name="Родитель")
    category = models.ForeignKey(
        CategoryMenu,
        on_delete=models.CASCADE, verbose_name="Категория меню")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'