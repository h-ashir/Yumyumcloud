from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'App/index.html')

def about(request):
    return render(request, 'App/about-yumyum.html')

def why_yumyum(request):
    return render(request, 'App/why-yumyum.html')

def photo(request):
    return render(request, 'App/photos.html')

def team(request):
    return render(request, 'App/team.html')

def catering(request):
    return render(request, 'App/catering.html')

def menu(request):
    return render(request, 'App/menu.html')

def contact(request):
    return render(request, 'App/contact.html')
