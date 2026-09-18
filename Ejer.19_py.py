# EJERCICIO 19 - Inventario de productos

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# productos y cantidades
# PROCESO:
# guardar/actualizar diccionario, validar, filtrar
# SALIDA:
# True/False, lista de productos
# Ejemplo de entrada:
# inv = Inventario()
# inv.agregar_stock("pan", 50)
# inv.restar_stock("pan", 30)
# inv.productos_bajo_stock(15)
# Salida esperada:
# True (en restar_stock)
# ["pan"] (en productos_bajo_stock, ya que 50 - 30 = 20... espera, 20 < 15 es False,
# pero si el stock queda en 20 o si probamos con un mínimo de 25, "pan" entra en la lista)

# 2. BOSQUEJO
# Instancia: inv = Inventario() -> self.stock = {}
#
# Método agregar_stock("pan", 50):
#   - Si "pan" existe en self.stock: sumar 50
#   - Si no existe: registrar self.stock["pan"] = 50
#
# Método restar_stock("pan", 30):
#   - Verificar si "pan" existe y si self.stock["pan"] >= 30
#   - Si cumple: restar 30 (queda 20) y retornar True
#   - Si no cumple: no restar y retornar False
#
# Método productos_bajo_stock(minimo):
#   - Iterar diccionario self.stock
#   - Si cantidad < minimo -> guardar nombre del producto en lista
#   - Retornar lista filtrada

# 3. PATRON
# Manejo de estado persistente usando un Diccionario como base de datos clave-valor `{producto: cantidad}`.
# Validación lógica previa antes de mutar/modificar valores internos (`self.stock[producto] >= cantidad`).
# Filtrado de colecciones mediante comprensión de listas `[prod for prod, cant in ...]`.


# 4. CODIGO
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
        bajo_stock = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                bajo_stock.append(producto)
        return bajo_stock


# 5. PRUEBA / DEPURACION
# Instanciación:
# inv = Inventario() -> self.stock = {}
#
# Paso 1: inv.agregar_stock("pan", 50)
#   - "pan" no está en stock -> self.stock["pan"] = 50
#
# Paso 2: inv.restar_stock("pan", 30)
#   - "pan" está en stock y 50 >= 30 -> True
#   - self.stock["pan"] = 50 - 30 = 20
#   - Retorna: True
#
# Paso 3: inv.productos_bajo_stock(25)
#   - Recorrer items: ("pan", 20)
#   - 20 < 25 -> True -> bajo_stock.append("pan")
#   - Retorna: ["pan"]