from django.contrib import admin
from .models.product import Product
from .models.category import categorie
from .models.customer import Customer
from .models.orders import Order


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'categorie']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

#this shows table in database
admin.site.register(Product,AdminProduct)
admin.site.register(categorie,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)

