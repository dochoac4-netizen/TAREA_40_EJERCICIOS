class Inventario:

    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [
            prod
            for prod, cant in self.stock.items()
            if cant < minimo
        ]


# --- Ejemplo de uso ---
inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.productos_bajo_stock(25))