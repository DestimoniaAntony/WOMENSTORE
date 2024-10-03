from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def shop2(request):
    return render(request, 'shop2.html')
def combine(request):
    return render(request, 'combine.html')

