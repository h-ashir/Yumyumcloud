from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about-yumyum/', views.about, name='about-yumyum'),
    path('why-yumyum', views.why_yumyum, name='why-yumyum'),

]