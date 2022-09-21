from django.contrib import admin

from .models import Country, Manufacturer, Car, Comment


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'start_year', 'end_year')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'car', 'created', 'author_email')
