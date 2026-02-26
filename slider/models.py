from django.db import models
from filer.fields.image import FilerImageField

class SliderItem(models.Model):
    title = models.CharField(
        "Название",
        max_length=255,
        help_text="Отображается в админке для удобства"
    )
    image = FilerImageField(
        verbose_name="Изображение",
        on_delete=models.CASCADE,
        related_name="slider_items"
    )
    # Поле для сортировки (обязательно для django-admin-sortable2)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок сортировки"
    )

    class Meta:
        verbose_name = "Элемент слайдера"
        verbose_name_plural = "Элементы слайдера"
        # Сортировка по умолчанию, чтобы drag-and-drop работал корректно
        ordering = ['my_order']

    def __str__(self):
        return str(self.title)
