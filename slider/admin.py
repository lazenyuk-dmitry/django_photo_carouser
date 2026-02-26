from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from .models import SliderItem

@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    # Что отображаем в списке
    list_display = ('my_order', 'display_image', 'title')
    # Делаем название ссылкой на редактирование
    list_display_links = ('display_image', 'title')

    def display_image(self, obj):
        """Метод для вывода превью картинки в списке"""
        if obj.image:
            # Используем .url, так как filer хранит объект файла
            return mark_safe(f'<img src="{obj.image.url}" width="80" style="border-radius: 5px;" />')
        return "Нет изображения"

    display_image.short_description = "Превью"
