from django.shortcuts import render
from .models import SliderItem

def index(request):
    slides = SliderItem.objects.all().order_by('my_order')
    return render(request, 'index.html', {'slides': slides})
