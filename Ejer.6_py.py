# EJERCICIO 6 - Estadísticas de temperatura

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# temperaturas individuales o en lote
# PROCESO:
# guardar, calcular mín, máx, promedio
# SALIDA:
# valores estadísticos
# Ejemplo de entrada:
# gt = GestorTemperatura()
# gt.registrar_multiples(20, 25, 18, 30)
# gt.promedio()
# Salida esperada:
# 23.25


# 2. BOSQUEJO
# Instancia: gt = GestorTemperatura() -> self.temperaturas = []
#
# Método registrar_temperatura(temp):
#   - Agregar a la lista interna: self.temperaturas.append(temp)
#
# Método registrar_multiples(*temps):
#   - Recorrer *temps y llamar a self.registrar_temperatura(t) por cada elemento
#
# Métodos estadísticos:
#   - minima(): min(self.temperaturas)
#   - maxima(): max(self.temperaturas)
#   - promedio(): sum(self.temperaturas) / len(self.temperaturas)


# 3. PATRON
# Acumulación de datos en una lista interna (`self.temperaturas`).
# Reutilización de métodos (`registrar_multiples` delega en `registrar_temperatura`).
# Uso de funciones built-in de Python (`min()`, `max()`, `sum()`, `len()`) para estadística básica.


# 4. CODIGO
class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

    def minima(self):
        if not self.temperaturas:
            return None
        return min(self.temperaturas)

    def maxima(self):
        if not self.temperaturas:
            return None
        return max(self.temperaturas)

    def promedio(self):
        if not self.temperaturas:
            return 0.0
        return sum(self.temperaturas) / len(self.temperaturas)


# 5. PRUEBA / DEPURACION
# Instanciación:
# gt = GestorTemperatura() -> self.temperaturas = []
#
# Ejecución 1: gt.registrar_multiples(20, 25, 18, 30)
# - Agrega secuencialmente 20, 25, 18, 30 mediante registrar_temperatura()
# - self.temperaturas = [20, 25, 18, 30]
#
# Ejecución 2: gt.promedio()
# - Suma = 20 + 25 + 18 + 30 = 93
# - Cantidad = 4
# - Promedio = 93 / 4 = 23.25
# Retorna: 23.25