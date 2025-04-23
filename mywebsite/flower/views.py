from django.shortcuts import render

# Create your views here.
from flower.models import Flower

from django.shortcuts import get_object_or_404


def flowers(request):
    q = request.GET.get('q', None)
    flowers = ''
    if q is None or q is "":
        flowers = Flower.objects.all()
    else:
        flowers = Flower.objects.filter(title__contains=q)
    return render(request, 'flower/flower.html', {'flowers': flowers})


def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'flower/detail.html', locals())
