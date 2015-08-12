from django.contrib import admin

from main.models import Manufacturer, Cereal, NutritionalFacts

# Register your models here.

admin.site.register(Cereal)
admin.site.register(Manufacturer)
admin.site.register(NutritionalFacts)