from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=150, verbose_name='Dni')
    fecha_nac = models.DateField(verbose_name='Fecha_nacimiento')
    direccion = models.CharField(max_length=150)
    sexo = models.CharField(max_length=20)

    def __str__(self):
        return f'Nombres: {self.nombres}, Apellidos: {self.apellidos}, Dni: {self.dni}, Fecha de nacimiento: {self.fecha_nac}, Direccion: {self.direccion}, Sexo: {self.sexo}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']


class Venta(models.Model):
    id_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now=True, verbose_name='Fecha_venta')
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Subtotal')
    iva = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Iva')
    total = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total')

    def __str__(self):
        return f'Id_cli: {self.id_cli}, Fecha de venta: {self.fecha_venta}, Subtotal: {self.subtotal}, Iva: {self.iva}, Total: {self.total}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'venta'
        ordering = ['id']


class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return f'Nombre: {self.nombre}'

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']


class Producto(models.Model):
    id_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagen/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Pvp')

    def __str__(self):
        return f'Id_cat: {self.id_cat}, nombre: {self.nombre}, Pvp: {self.pvp}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']


class DetVenta(models.Model):
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio')
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Subtotal')

    def __str__(self):
        return f'Id_prod: {self.id_prod}, Id_venta: {self.id_venta}, Cantidad: {self.cantidad}, Precio: {self.precio}, Subtotal: {self.subtotal}'

    class Meta:
        verbose_name = 'Detalle_Venta'
        verbose_name_plural = 'Detalles_Ventas'
        db_table = 'detalle_venta'
        ordering = ['id']
