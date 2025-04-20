from django.shortcuts import render

# Create your views here.
from flower.models import Flower

from django.shortcuts import get_object_or_404


def flowers(request):
    flowers = Flower.objects.all()
    return render(request, 'flower/flower.html', {'flowers': flowers})


def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'flower/detail.html', locals())
