# EJERCICIO 18 - Matriz de distancias

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# tuplas (x, y) como puntos
# PROCESO:
# calcular distancia con fórmula, comparar, guardar
# SALIDA:
# distancia numérica, punto más cercano
# Ejemplo de entrada:
# cd = CalculadorDistancia()
# cd.distancia_euclidiana((0,0), (3,4))
# Salida esperada:
# 5.0

# 2. BOSQUEJO
# Instancia: cd = CalculadorDistancia() -> self.distancias = []
#
# Método distancia_euclidiana((0,0), (3,4)):
#   - Aplicar fórmula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
#   - d = sqrt((3 - 0)^2 + (4 - 0)^2) = sqrt(9 + 16) = sqrt(25) = 5.0
#   - Guardar en lista de historial: self.distancias.append(d)
#   - Retornar 5.0
#
# Método punto_mas_cercano((0,0), (1,1), (3,4)):
#   - Comparar la distancia desde la referencia (0,0) a cada punto de *puntos.
#   - Distancia a (1,1) = 1.41
#   - Distancia a (3,4) = 5.0
#   - Retornar el punto con la distancia mínima: (1,1)

# 3. PATRON
# Uso del módulo matemático `math.sqrt()` para el cálculo geométrico de la raíz cuadrada.
# Manejo de coordenadas mediante desestructuración de tuplas `(x1, y1) = p1`.
# Búsqueda de un elemento mínimo iterando y comparando sobre un grupo variable de tuplas (`*puntos`).


# 4. CODIGO
import math


class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None

        mas_cercano = None
        distancia_minima = float("inf")

        for punto in puntos:
            dist = self.distancia_euclidiana(referencia, punto)
            if dist < distancia_minima:
                distancia_minima = dist
                mas_cercano = punto

        return mas_cercano


# 5. PRUEBA / DEPURACION
# Instanciación:
# cd = CalculadorDistancia() -> self.distancias = []
#
# Ejecución: cd.distancia_euclidiana((0,0), (3,4))
# Paso 1: p1 = (0, 0) -> x1 = 0, y1 = 0
# Paso 2: p2 = (3, 4) -> x2 = 3, y2 = 4
# Paso 3: (3 - 0)**2 + (4 - 0)**2 = 9 + 16 = 25
# Paso 4: math.sqrt(25) = 5.0
# Paso 5: self.distancias.append(5.0)
# Resultado devuelto: 5.0