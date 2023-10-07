from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import update_session_auth_hash
from .models import Producto
from .models import Carrito
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


def index(request):
    return render(request, 'StoreGames/index.html')

def cierresesion(request):
    return render(request, 'StoreGames/html/cierresesion.html')

def bienvenida(request):
    return render(request, 'StoreGames/html/bienvenida.html')

def index_admin(request):
    return render(request, 'StoreGames/index_admin.html')

def aventura(request):
    productos = Producto.objects.filter(categoria_id=1)
    
    context = {
        'productos': productos
    }
    return render(request, 'StoreGames/html/aventura.html', context)


def carreras(request):
    productos = Producto.objects.filter(categoria_id=3)
    
    context = {
        'productos': productos
    }
    return render(request, 'StoreGames/html/carreras.html', context)

def deportes(request):
    productos = Producto.objects.filter(categoria_id=4)
    
    context = {
        'productos': productos
    }

    return render(request, 'StoreGames/html/deportes.html', context)

def rol(request):
    productos = Producto.objects.filter(categoria_id=5)
    
    context = {
        'productos': productos
    }
    return render(request, 'StoreGames/html/rol.html',context)

def shooter(request):
    productos = Producto.objects.filter(categoria_id=2)
    
    context = {
        'productos': productos
    }

    return render(request, 'StoreGames/html/shooter.html', context)

def editar(request):
    return render(request, 'StoreGames/html/editar_perfil.html')

def realizar_pedido(request):
    return render(request, 'StoreGames/html/realizar_pedido.html')

def loginc(request):
    return render(request, 'StoreGames/html/login.html')

def recuperar(request):
    return render(request, 'StoreGames/html/recuperar.html')

def panel_control_admi(request):
    return render(request, 'StoreGames/html/panel_control_admi.html')

def ingresarcontenido(request):
    return render(request, 'StoreGames/html/ingresarcontenido.html')


def registro(request):
    return render(request, 'StoreGames/html/registro.html')

def cambio_contra(request):
    return render(request, 'StoreGames/html/cambio_contrasena.html')

def compra_finalizada(request):
    return render(request, 'StoreGames/html/compra_finalizada.html')


#CARRITO
def carrito(request):
  
    carrito_items = Carrito.objects.filter(usuario=request.user)
    context = {
        'carrito_items': carrito_items,
    }
    return render(request, 'StoreGames/html/carrito.html', context)

#EDITAR PERFIL
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        usuario = request.user
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        email = request.POST['email']
        nuevo_username = request.POST['usuario']

        try:
           
            existing_user = Usuario.objects.exclude(pk=usuario.pk).filter(username=nuevo_username).exists()
            existing_email = Usuario.objects.exclude(pk=usuario.pk).filter(email=email).exists()

            if existing_user:
                error_message = "El nombre de usuario ya está en uso. Por favor, elige otro."
            elif existing_email:
                error_message = "El correo electrónico ya está en uso. Por favor, utiliza otro."
            else:
                # Actualizar los datos del usuario
                usuario.username = nuevo_username
                usuario.nombre = nombre
                usuario.apellidos = apellidos
                usuario.email = email
                usuario.save()
                messages.success(request, 'Perfil actualizado exitosamente.')
                return redirect('index')
        except IntegrityError as e:
            error_message = "Ha ocurrido un error durante la actualización. Por favor, inténtalo nuevamente."

        messages.error(request, error_message)

    return render(request, 'StoreGames/html/editar_perfil.html')

#CAMBIAR CONTRASENA
@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        usuario = request.user
        contrasena_antigua = request.POST['contrasena_antigua']
        nueva_contrasena = request.POST['nueva_contrasena']
        verificacion_contrasena = request.POST['verificacion_contrasena']

        try: 
            if usuario.check_password(contrasena_antigua):
                if nueva_contrasena == verificacion_contrasena:
                    usuario.set_password(nueva_contrasena)
                    usuario.save()
                    update_session_auth_hash(request, usuario)  
                    messages.success(request, 'Contraseña cambiada exitosamente.')
                    return redirect('cambiar_contrasena')
                else:
                    error_message = "Las contraseñas no coinciden."
            else:
                error_message = "La contraseña antigua no es válida."
        except IntegrityError as e:
            error_message = "Ha ocurrido un error al cambiar la contraseña. Por favor, inténtalo nuevamente."

        messages.error(request, error_message)

    return render(request, 'StoreGames/html/cambio_contrasena.html')




#VISTA DE REGISTRAR USUARIO
def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        email = request.POST['correo']
        username = request.POST['user']
        password = request.POST['pass']
        
        try:
           
            existing_user = Usuario.objects.filter(username=username).exists()
            existing_email = Usuario.objects.filter(email=email).exists()
            
            if existing_user:
                error_message = "El nombre de usuario ya está en uso. Por favor, elige otro."
            elif existing_email:
                error_message = "El correo electrónico ya está en uso. Por favor, utiliza otro."
            else:
                
                usuario_nuevo = Usuario(
                    username=username,
                    password=password,
                    email=email,
                    nombre=nombre,
                    apellidos=apellidos,
                )
                usuario_nuevo.set_password(password)
                usuario_nuevo.save()
                # Iniciar sesión al usuario recién registrado
                login(request, usuario_nuevo)
                return redirect('bienvenida')
        except IntegrityError as e:
            error_message = "Ha ocurrido un error durante el registro. Por favor, inténtalo nuevamente."
        
        return render(request, 'StoreGames/html/registro.html', {'error_message': error_message})
    
    return render(request, 'StoreGames/html/registro.html')



# INICAR SESION
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'StoreGames/html/login.html', {'error_message': error_message})
    return render(request, 'StoreGames/html/login.html')



#AGREGAR UNIDADES AL CARRITO

def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)

    if request.user.is_authenticated:
        cantidad = int(request.POST.get('cantidad', 1))

        if cantidad <= producto.stockProd:
            precio_total = producto.precioProducto * cantidad
            carrito, created = Carrito.objects.get_or_create(usuario=request.user, producto=producto)

            if (carrito.cantidad + cantidad) <= producto.stockProd:
                carrito.cantidad += cantidad
                carrito.precio_total = precio_total
                carrito.save()
                messages.success(request, "Producto agregado al carrito correctamente.")
            else:
                messages.error(request, "La cantidad solicitada supera el stock disponible en el carrito.")
        else:
            messages.error(request, "La cantidad solicitada supera el stock disponible.")
    else:
        messages.warning(request, "Debes iniciar sesión para agregar productos al carrito.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # se regresa a la misma pagian donde esta



#FUNCIONP QUITAR STOCK EN CARRITO
def disminuir_unidad(request, carrito_id):
    item = Carrito.objects.get(id=carrito_id, usuario=request.user)
    if item.cantidad > 1:  # Si hay más de una unidad, disminuye
        item.cantidad -= 1
        item.precio_total -= item.producto.precioProducto  #
        item.save()
    else:  
        item.delete()
    return redirect('carrito')

#FUNCION PARA VACIAR CARRITO
def vaciar_carrito(request):
    Carrito.objects.filter(usuario=request.user).delete()
    return redirect('carrito')





#FUNCION PARA FINALIZAR COMPRA
def finalizar_compra(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)

    for item in carrito_items:
        producto = item.producto
        producto.stockProd -= item.cantidad
        producto.save()

    
    carrito_items.delete()

    return redirect('compra_finalizada')  
