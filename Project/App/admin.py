from django.contrib import admin
from App.models import Contact_Detail, Photo, Outlet, Team_line_1, Team_line_2
# Register your models here.

admin.site.register(Contact_Detail)
admin.site.register(Photo)
admin.site.register(Team_line_1)
admin.site.register(Team_line_2)

class Outlet_Display(admin.ModelAdmin):
    list_display = ['id', 'outlet_main_title', 'outlet_name']
admin.site.register(Outlet, Outlet_Display)