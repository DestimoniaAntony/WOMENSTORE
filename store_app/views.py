from django.shortcuts import render

# Create your views here.
# def index(request):
#     return render(request, 'index.html')
# def shop2(request):
#     return render(request, 'shop2.html')
# def combine(request):
#     return render(request, 'combine.html')

from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    # Instead of using FileResponse, use render to serve HTML templates
    return render(request, 'index.html')