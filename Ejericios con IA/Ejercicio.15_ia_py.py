# Ej. 15 BÁSICO  Divisores de un número

# Clase DivisorFinder que: (1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores; (2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; (3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.

# ENTRADA
# uno o varios números

# PROCESO
# encontrar divisores con bucles, verificar suma

# SALIDA
# tuplas, booleano, diccionario

# EJEMPLO DE ENTRADA
# df = DivisorFinder()
# df.encontrar_divisores(12)

# SALIDA ESPERADA
# (1, 2, 3, 4, 6, 12)

# Colecciones: tuplas (inmutables), diccionario como almacén


class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        # Excluimos el propio número
        divisores_propios = divisores[:-1]
        return sum(divisores_propios) == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for num in numeros:
            resultado[num] = self.encontrar_divisores(num)
        return resultado


# DEPURACIÓN / PRUEBA DE ESCRITORIO
# df = DivisorFinder()

# 1. Probar encontrar_divisores:
# df.encontrar_divisores(12)
# -> i = 1..12: 12 % i == 0 para i in [1, 2, 3, 4, 6, 12]
# -> Retorna tupla: (1, 2, 3, 4, 6, 12)

# 2. Probar es_perfecto:
# df.es_perfecto(6)
# -> encontrar_divisores(6) -> (1, 2, 3, 6)
# -> divisores_propios -> (1, 2, 3)
# -> sum((1, 2, 3)) == 6 -> 6 == 6 -> Retorna True

# 3. Probar encontrar_multiples_divisores:
# df.encontrar_multiples_divisores(6, 12)
# -> num = 6:  resultado[6]  = (1, 2, 3, 6)
# -> num = 12: resultado[12] = (1, 2, 3, 4, 6, 12)
# -> Retorna: {6: (1, 2, 3, 6), 12: (1, 2, 3, 4, 6, 12)}