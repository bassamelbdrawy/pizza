from django.contrib import admin
from .models import Regular_pizza,Sicilian_pizza,Topping,Sub,Salad,Dinner_platter,Pasta,my_order

# Register your models here.

admin.site.register(Regular_pizza)
admin.site.register(Sicilian_pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_platter)
admin.site.register(my_order)
