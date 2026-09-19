# Ej. 19 BÁSICO  Inventario de productos

# Clase Inventario que: (1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; (2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; (3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.

# ENTRADA
# productos y cantidades

# PROCESO
# guardar/actualizar diccionario, validar, filtrar

# SALIDA
# True/False, lista de productos

# EJEMPLO DE ENTRADA
# inv = Inventario()
# inv.agregar_stock("pan", 50)
# inv.restar_stock("pan", 30)
# inv.productos_bajo_stock(15)

# SALIDA ESPERADA
# True
# ["pan"]

# Colecciones: diccionario como base de datos simple


class Inventario:

    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        bajos = []
        for prod, cant in self.stock.items():
            if cant < minimo:
                bajos.append(prod)
        return bajos


# DEPURACIÓN
# inv = Inventario() -> stock = {}
# inv.agregar_stock("pan", 50) -> stock = {"pan": 50}
# inv.restar_stock("pan", 30) -> 50 >= 30 -> stock = {"pan": 20} -> Retorna True
# inv.productos_bajo_stock(25) -> "pan": 20 < 25 -> Retorna ["pan"]