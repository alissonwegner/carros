from django.contrib import admin
from .models import Car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    #
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    #
    search_fields = ('model', 'brand',)
    #search_fields campo de busca. Está dizendo que quando pesquisar vai  pesquisar no model

admin.site.register(Brand, BrandAdmin) 
admin.site.register(Car, CarAdmin )