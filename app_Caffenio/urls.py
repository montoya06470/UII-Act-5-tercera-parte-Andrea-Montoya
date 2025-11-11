# app_Caffenio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Inicio
    path('', views.inicio_caffenio, name='inicio'),

    # Proveedores
    path('proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/realizar-actualizacion/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),

    # Productos
    path('productos/', views.ver_productos, name='ver_productos'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/realizar-actualizacion/<int:id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),

    # Ventas
    path('ventas/', views.ver_ventas, name='ver_ventas'),
    path('venta/agregar/', views.agregar_venta, name='agregar_venta'),
    path('venta/actualizar/<int:id>/', views.actualizar_venta, name='actualizar_venta'),
    path('venta/realizar-actualizacion/<int:id>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('venta/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),
]