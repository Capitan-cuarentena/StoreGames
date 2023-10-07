from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, username, email, password=None, nombre=None, apellidos=None):
        usuario = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        usuario.is_superuser = True
        usuario.is_staff = True
        if nombre is not None:
            usuario.nombre = nombre
        if apellidos is not None:
            usuario.apellidos = apellidos
        usuario.save(using=self._db)
        return usuario

    def get_by_natural_key(self, username):
        return self.get(username=username)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    apellidos = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False)  

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellidos']

    objects = UsuarioManager()

class Categoria (models.Model):
    idCategoria = models.AutoField(primary_key=True,verbose_name="ID de la categoria")
    nombreCat = models.CharField(max_length=30,verbose_name="Nombre de la categoria",null=False, blank=False)
    def __str__(self):
        return self.nombreCat    


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Id del Producto")
    nombreProducto = models.CharField(max_length=50, verbose_name="Nombre del Producto", null=False, blank=False)
    precioProducto = models.IntegerField(verbose_name="Precio del Producto", null=False, blank=False)
    descripcionProducto = models.CharField(max_length=900, verbose_name="Descripcion del Producto", null=False, blank=False)
    stockProd = models.IntegerField(verbose_name="Stock del Producto", null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)


    class Meta:
        db_table = 'STOREGAMES_PRODUCTO'  

    def __str__(self):
        return f"{self.nombreProducto} - ${self.precioProducto}"



class Venta (models.Model):
    idVenta = models.AutoField(primary_key=True,verbose_name="Id de venta",null=False, blank=False)
    fechaVenta = models.DateField(verbose_name="Id de venta",null=False, blank=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    def __str__(self):
        return self.fechaVenta    



class Detalle (models.Model):
    idDetalle = models.AutoField(primary_key=True,verbose_name="Id del detalle",null=False, blank=False)
    cantidad = models.IntegerField(verbose_name="Cantidad",null=False, blank=False)
    subTotal = models.IntegerField(verbose_name="Subtotal",null=False, blank=False)
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    def __str__(self):
        return self.subTotal




class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  

    def __str__(self):
        return f"{self.usuario} - {self.producto} - Cantidad: {self.cantidad} - Precio Total: {self.precio_total}"
