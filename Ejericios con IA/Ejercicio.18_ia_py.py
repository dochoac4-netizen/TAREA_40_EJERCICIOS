# Ej. 18 MEDIO  Calculador de puntos

# Clase CalculadorOrigen que: (1) tenga método distancia_origen(p) que reciba una tupla (x,y) y calcule la distancia al origen (0,0); (2) tenga método punto_mas_lejano(*puntos) que retorne el punto más lejano; (3) tenga un atributo lista para guardar todas las distancias calculadas.

# ENTRADA
# tuplas (x, y) como puntos

# PROCESO
# calcular distancia con fórmula, comparar, guardar

# SALIDA
# distancia numérica, punto más lejano

# EJEMPLO DE ENTRADA
# co = CalculadorOrigen()
# co.distancia_origen((3, 4))

# SALIDA ESPERADA
# 5.0

# Colecciones: tuplas como puntos 2D; lista para guardar resultados

import math


class CalculadorOrigen:

    def __init__(self):
        self.distancias = []

    def distancia_origen(self, p):
        d = math.sqrt(p[0]**2 + p[1]**2)
        self.distancias.append(d)
        return d

    def punto_mas_lejano(self, *puntos):
        lejano = puntos[0]
        max_d = self.distancia_origen(puntos[0])

        for p in puntos:
            d = self.distancia_origen(p)
            if d > max_d:
                max_d = d
                lejano = p

        return lejano


# DEPURACIÓN
# co = CalculadorOrigen()
# co.distancia_origen((3, 4)) -> d = sqrt(9 + 16) = 5.0 -> distancias = [5.0] -> Retorna 5.0
# co.punto_mas_lejano((1, 1), (3, 4))
# -> p=(1, 1): d = 1.41
# -> p=(3, 4): d = 5.0 (5.0 > 1.41)
# -> Retorna (3, 4)