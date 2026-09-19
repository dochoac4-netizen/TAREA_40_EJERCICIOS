# Ej. 12 MEDIO  Selector de rango con tuplas

# Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango; (2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio, fin) y retorne una lista combinada sin duplicados usando un conjunto.

# ENTRADA
# pares (inicio, fin) para varios rangos

# PROCESO
# crear rangos como tuplas, unir sin duplicados

# SALIDA
# lista de elementos únicos

# EJEMPLO DE ENTRADA
# sr = SelectorRango()
# sr.elementos_en_multiples_rangos((1,3), (2,4))

# SALIDA ESPERADA
# [1, 2, 3, 4]

# Colecciones: tuplas como parámetros + conjuntos para eliminar duplicados


class SelectorRango:

    def crear_rango(self, inicio, fin):
        numeros = []
        for i in range(inicio, fin + 1):
            numeros.append(i)
        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):
        unicos = set()
        for inicio, fin in rangos:
            tupla_rango = self.crear_rango(inicio, fin)
            for num in tupla_rango:
                unicos.add(num)
        return sorted(list(unicos))


# DEPURACIÓN / PRUEBA DE ESCRITORIO
# sr = SelectorRango()

# 1. Probar crear_rango:
# sr.crear_rango(1, 3)
# -> range(1, 4) -> i = 1, 2, 3
# -> Retorna tupla: (1, 2, 3)

# 2. Probar elementos_en_multiples_rangos:
# sr.elementos_en_multiples_rangos((1,3), (2,4))
# -> unicos = set()
# -> Iteración 1: inicio=1, fin=3 -> crear_rango(1, 3) -> (1, 2, 3) -> unicos = {1, 2, 3}
# -> Iteración 2: inicio=2, fin=4 -> crear_rango(2, 4) -> (2, 3, 4) -> unicos = {1, 2, 3, 4}
# -> Retorna lista ordenada: [1, 2, 3, 4]