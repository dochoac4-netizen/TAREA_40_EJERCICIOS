# EJERCICIO 3 - GESTOR DE INVENTARIO CON VALORACIÓN

# 1. ENTENDER EL PROBLEMA
# ENTRADA: productos y cantidades
# PROCESO: guardar en diccionario {producto: cantidad}, sumar cantidades, filtrar por rango
# SALIDA: total de stock, productos en rango
# Ejemplo de entrada:
# i = Inventario()
# i.agregar_producto("manzanas", 10)
# i.agregar_producto("peras", 5)
# i.total_stock()
# Salida esperada: 15


# 2. BOSQUEJO
# self.productos = {}
# agregar("manzanas", 10) -> {"manzanas": 10}
# agregar("peras", 5) -> {"manzanas": 10, "peras": 5}
# total_stock() -> sum([10, 5]) = 15
# productos_por_rango(4, 8) -> ["peras"]


# 3. PATRON
# Diccionario clave-valor {producto: cantidad}, sum() sobre .values() e iteración con .items() para filtrar.


# 4. CODIGO
class Inventario:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def total_stock(self):
        return sum(self.productos.values())

    def productos_por_rango(self, cant_min, cant_max):
        rango = []
        for nombre, cantidad in self.productos.items():
            if cant_min <= cantidad <= cant_max:
                rango.append(nombre)
        return rango


# 5. PRUEBA / DEPURACION
# i = Inventario() -> self.productos = {}
# agregar_producto("manzanas", 10) -> self.productos = {"manzanas": 10}
# agregar_producto("peras", 5) -> self.productos = {"manzanas": 10, "peras": 5}
# total_stock() -> sum([10, 5]) -> 15
# productos_por_rango(4, 8) -> ("peras", 5) entra en rango -> Retorna ["peras"]