from django.shortcuts import render
from images.models import FeaturedImage
from django.conf import settings

def home(request):
    print(settings.STATIC_ROOT)
    return render(request, 'images/home.html')
