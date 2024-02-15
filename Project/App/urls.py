from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about-yumyum/', views.about, name='about-yumyum'),
    path('why-yumyum/', views.why_yumyum, name='why-yumyum'),
    path('contact-us/', views.contact, name='contact-us'),
    # path('menu/', views.menu, name='menu'),
    # path('photo/', views.photo, name='photo'),
    # path('contact-us/', views.contact, name='contact-us'),

]