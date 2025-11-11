# app_Caffenio/admin.py
from django.contrib import admin
from .models import Proveedor, Producto, Venta

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta)