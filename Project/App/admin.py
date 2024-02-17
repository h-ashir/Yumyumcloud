from django.contrib import admin
from App.models import Contact_Detail, Photo, Outlet
# Register your models here.

admin.site.register(Contact_Detail)
admin.site.register(Photo)

class Outlet_Display(admin.ModelAdmin):
    list_display = ['id', 'outlet_main_title', 'outlet_name']
admin.site.register(Outlet, Outlet_Display)