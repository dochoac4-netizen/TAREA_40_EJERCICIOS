# EJERCICIO DE PRÁCTICA - MAPEADOR DE PRECIOS

# 1. ENTENDER EL PROBLEMA
# ENTRADA: productos y precios
# PROCESO: guardar en diccionario, filtrar, promediar
# SALIDA: lista filtrada, promedio
# EJEMPLO DE ENTRADA:
# gp = GestorProductos()
# gp.agregar_producto("Laptop", 1200)
# gp.agregar_producto("Mouse", 25)
# gp.productos_caros(100)
# SALIDA ESPERADA:
# ["Laptop"]


# 2. BOSQUEJO
# Agregar ("Laptop", 1200) y ("Mouse", 25):
#   self.productos = {"Laptop": 1200, "Mouse": 25}
#
# Filtrar productos_caros(100):
#   Laptop: 1200 >= 100 -> True  -> ["Laptop"]
#   Mouse:  25 >= 100   -> False -> descarta
#   Lista filtrada: ["Laptop"]
#
# Precio promedio:
#   (1200 + 25) / 2 = 1225 / 2 -> 612.5


# 3. PATRON
# Colecciones: diccionario producto->precio, iteración con items()


# 4. CODIGO
class GestorProductos:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, precio):
        self.productos[producto] = precio

    def productos_caros(self, precio_minimo):
        filtrados = []
        for producto, precio in self.productos.items():
            if precio >= precio_minimo:
                filtrados.append(producto)
        return filtrados

    def precio_promedio(self):
        if not self.productos:
            return 0
        return sum(self.productos.values()) / len(self.productos)


# 5. PRUEBA / DEPURACION
# gp = GestorProductos() -> self.productos = {}

# agregar_producto("Laptop", 1200) -> self.productos = {"Laptop": 1200}
# agregar_producto("Mouse", 25)    -> self.productos = {"Laptop": 1200, "Mouse": 25}

# productos_caros(100)
# "Laptop": 1200 >= 100 -> True  -> filtrados = ["Laptop"]
# "Mouse":  25 >= 100   -> False -> descarta
# Retorna: ["Laptop"]

# precio_promedio()
# sum(values) = 1225
# len(productos) = 2
# 1225 / 2 -> Retorna: 612.5