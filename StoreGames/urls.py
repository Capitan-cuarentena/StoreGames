from django.urls import path
from . import views
from .views import iniciar_sesion
from django.contrib.auth import views as auth_views
from .models import Usuario
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('index_admin/', views.index_admin, name="index_admin"),
    path('aventura/', views.aventura, name="aventura"),
    path('bienvenida/', views.bienvenida, name="bienvenida"),
    path('cierresesion/', views.cierresesion, name="cierresesion"),
    path('carreras/', views.carreras, name="carreras"),
    path('deportes/', views.deportes, name="deportes"),
    path('rol/', views.rol, name="rol"),
    path('shooter/', views.shooter, name="shooter"),
    path('registro/', views.registro, name="registro"), 
    path('recuperar/', views.recuperar, name="recuperar"),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('editarperfil/', views.editar_perfil, name='editarperfil'),
    path('panel_control_admi/', views.panel_control_admi, name="panel_control_admi"),
    path('logout/', auth_views.LogoutView.as_view(next_page='cierresesion'), name='logout'),
    path('ingresarcontenido/', views.ingresarcontenido, name="ingresarcontenido"),
    path('editar/', views.editar, name="editar"),
    path('loginc/', views.loginc, name='loginc'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'), 
    path('cambio_contra/', views.cambio_contra, name='cambio_contra'),
    path('cambiar_contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('realizar_pedido/', views.realizar_pedido, name='realizar_pedido'),
    path('carrito/disminuir/<int:carrito_id>/', views.disminuir_unidad, name='disminuir_unidad'),
    path('carrito/vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('carrito/finalizar/', views.finalizar_compra, name='finalizar_compra'),
    path('compra_finalizada/', views.compra_finalizada, name='compra_finalizada'),
]

#esto es para guardar imagenes en BD
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)