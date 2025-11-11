# app_Caffenio/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Producto, Venta

# ==================== INICIO ====================
def inicio_caffenio(request):
    return render(request, 'inicio.html')

# ==================== PROVEEDORES ====================
def agregar_proveedor(request):
    if request.method == 'POST':
        Proveedor.objects.create(
            nombre=request.POST['nombre'],
            empresa=request.POST['empresa'],
            telefono=request.POST['telefono'],
            correo=request.POST['correo'],
            direccion=request.POST['direccion'],
            pais=request.POST['pais'],
            tipo_producto=request.POST['tipo_producto']
        )
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.empresa = request.POST['empresa']
        proveedor.telefono = request.POST['telefono']
        proveedor.correo = request.POST['correo']
        proveedor.direccion = request.POST['direccion']
        proveedor.pais = request.POST['pais']
        proveedor.tipo_producto = request.POST['tipo_producto']
        proveedor.save()
        return redirect('ver_proveedores')
    return redirect('actualizar_proveedor', id=id)

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# ==================== PRODUCTOS ====================
def agregar_producto(request):
    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            categoria=request.POST['categoria'],
            proveedor_id=request.POST['proveedor'],
            sucursal=request.POST['sucursal']
        )
        return redirect('ver_productos')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_producto.html', {'productos': productos})

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto,
        'proveedores': proveedores
    })

def realizar_actualizacion_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.categoria = request.POST['categoria']
        producto.proveedor_id = request.POST['proveedor']
        producto.sucursal = request.POST['sucursal']
        producto.save()
        return redirect('ver_productos')
    return redirect('actualizar_producto', id=id)

def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# ==================== VENTAS ====================
def agregar_venta(request):
    if request.method == 'POST':
        venta = Venta.objects.create(
            cliente=request.POST['cliente'],
            total=request.POST['total'],
            metodo_pago=request.POST['metodo_pago'],
            sucursal=request.POST['sucursal'],
            empleado=request.POST['empleado']
        )
        productos_ids = request.POST.getlist('productos')
        venta.productos.set(productos_ids)
        venta.save()
        return redirect('ver_ventas')
    productos = Producto.objects.all()
    return render(request, 'venta/agregar_venta.html', {'productos': productos})

def ver_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/ver_venta.html', {'ventas': ventas})

def actualizar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    productos = Producto.objects.all()
    return render(request, 'venta/actualizar_venta.html', {
        'venta': venta,
        'productos': productos
    })

def realizar_actualizacion_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.cliente = request.POST['cliente']
        venta.total = request.POST['total']
        venta.metodo_pago = request.POST['metodo_pago']
        venta.sucursal = request.POST['sucursal']
        venta.empleado = request.POST['empleado']
        productos_ids = request.POST.getlist('productos')
        venta.productos.set(productos_ids)
        venta.save()
        return redirect('ver_ventas')
    return redirect('actualizar_venta', id=id)

def borrar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})