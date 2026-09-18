# EJERCICIO 3 - Gestor de compras con totales

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# nombres de artículos y precios
# PROCESO:
# guardar en diccionario, sumar valores, filtrar por rango
# SALIDA:
# total, artículos en rango
# Ejemplo de entrada:
# c = CarroCompras()
# c.agregar_articulo("pan", 2.50)
# c.agregar_articulo("leche", 3.00)
# c.total_carrito()
# Salida esperada:
# 5.50


# 2. BOSQUEJO
# Instancia: c = CarroCompras() -> self.articulos = {}
#
# Método agregar_articulo("pan", 2.50):
#   - Asignar clave-valor en diccionario: self.articulos["pan"] = 2.50
#
# Método total_carrito():
#   - Sumar todos los valores de los precios con sum(self.articulos.values())
#   - sum([2.50, 3.00]) = 5.50
#
# Método articulos_por_rango(precio_min, precio_max):
#   - Recorrer items del diccionario (nombre, precio)
#   - Filtrar si precio_min <= precio <= precio_max
#   - Retornar lista con los nombres de los artículos filtrados


# 3. PATRON
# Uso de Diccionario (`dict`) como estructura clave-valor `{articulo: precio}`.
# Uso de `.values()` para iterar directo sobre los precios y calcular totales con `sum()`.
# Filtrado mediante iteración de `.items()` para obtener nombres de artículos dentro de un rango de precios.


# 4. CODIGO
class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        filtrados = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                filtrados.append(nombre)
        return filtrados


# 5. PRUEBA / DEPURACION
# Instanciación:
# c = CarroCompras() -> self.articulos = {}
#
# Ejecución 1: c.agregar_articulo("pan", 2.50)
# - self.articulos = {"pan": 2.50}
#
# Ejecución 2: c.agregar_articulo("leche", 3.00)
# - self.articulos = {"pan": 2.50, "leche": 3.00}
#
# Ejecución 3: c.total_carrito()
# - sum([2.50, 3.00]) = 5.50
# Retorna: 5.50