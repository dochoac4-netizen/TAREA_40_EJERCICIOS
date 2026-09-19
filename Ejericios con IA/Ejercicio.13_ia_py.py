# Ej. 13 BÁSICO  Combinador de listas

# Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; (2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.

# ENTRADA
# dos o más listas

# PROCESO
# alternar elementos con índices, bucles

# SALIDA
# lista intercalada

# EJEMPLO DE ENTRADA
# cl = CombinadorListas()
# cl.intercalar([1,2], [3,4])

# SALIDA ESPERADA
# [1, 3, 2, 4]

# Colecciones: indexación de listas con loops y condicionales


class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []
        max_len = max(len(lista1), len(lista2))
        for i in range(max_len):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []

        resultado = listas[0]
        for lista_siguiente in listas[1:]:
            resultado = self.intercalar(resultado, lista_siguiente)
        return resultado

# DEPURACIÓN / PRUEBA DE ESCRITORIO
# cl = CombinadorListas()

# 1. Probar intercalar:
# cl.intercalar([1, 2], [3, 4])
# -> max_len = max(2, 2) = 2
# -> i = 0: 0 < len(lista1) -> append(1), 0 < len(lista2) -> append(3) -> resultado = [1, 3]
# -> i = 1: 1 < len(lista1) -> append(2), 1 < len(lista2) -> append(4) -> resultado = [1, 3, 2, 4]
# -> Retorna: [1, 3, 2, 4]

# 2. Probar intercalar_multiples:
# cl.intercalar_multiples([1, 2], [3, 4], [5, 6])
# -> resultado inicial = [1, 2]
# -> Iteración 1: self.intercalar([1, 2], [3, 4]) -> resultado = [1, 3, 2, 4]
# -> Iteración 2: self.intercalar([1, 3, 2, 4], [5, 6]) -> resultado = [1, 5, 3, 6, 2, 4]
# -> Retorna: [1, 5, 3, 6, 2, 4]