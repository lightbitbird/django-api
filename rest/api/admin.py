from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Author, Book, FoodStuff, Nutrients, Taxes, States, Countries

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Countries)
admin.site.register(States)
admin.site.register(Taxes)
admin.site.register(Nutrients)
admin.site.register(FoodStuff)
