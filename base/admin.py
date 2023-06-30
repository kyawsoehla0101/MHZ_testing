from django.contrib import admin
from . models import *

# Register your models here.
class AdminCoffee(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'image']
admin.site.register(Coffee, AdminCoffee)