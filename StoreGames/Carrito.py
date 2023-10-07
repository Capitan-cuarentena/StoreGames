from .models import Producto

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto_id):
        producto = Producto.objects.get(pk=producto_id)
        id = str(producto_id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto_id,
                "nombre": producto.nombreProducto,
                "acumulado": producto.precioProducto,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precioProducto
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto_id):
        id = str(producto_id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto_id):
        id = str(producto_id)
        if id in self.carrito.keys():
            producto = Producto.objects.get(pk=producto_id)
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precioProducto
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto_id)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
