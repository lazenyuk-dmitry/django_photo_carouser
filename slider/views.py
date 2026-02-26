from django.shortcuts import render
from .models import SliderItem

def index(request):
    # Получаем все слайды, отсортированные по my_order
    slides = SliderItem.objects.all().order_by('my_order')
    return render(request, 'index.html', {'slides': slides})
