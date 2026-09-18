# EJERCICIO 13 - Combinador de listas

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# dos o más listas
# PROCESO:
# alternar elementos con índices, bucles
# SALIDA:
# lista intercalada
# Ejemplo de entrada:
# cl = CombinadorListas()
# cl.intercalar([1, 2], [3, 4])
# Salida esperada:
# [1, 3, 2, 4]

# 2. BOSQUEJO
# Instancia: cl = CombinadorListas()
#
# Método intercalar([1, 2], [3, 4]):
#   - Determinar la longitud máxima entre ambas listas -> max(2, 2) = 2
#   - Iterar con i desde 0 hasta 1:
#       * i = 0: agregar lista1[0] (1), agregar lista2[0] (3) -> [1, 3]
#       * i = 1: agregar lista1[1] (2), agregar lista2[1] (4) -> [1, 3, 2, 4]
#   - Retornar [1, 3, 2, 4]
#
# Método intercalar_multiples(*listas):
#   - Recibir varias listas (ej: l1, l2, l3)
#   - Iniciar resultado con la primera lista (l1)
#   - Reutilizar el método intercalar con las demás listas secuencialmente:
#       * resultado = intercalar(resultado, l2)
#       * resultado = intercalar(resultado, l3)
#   - Retornar resultado intercalado completo.

# 3. PATRON
# Uso de bucle `for` controlado por índice `i` mediante `range(max_len)`.
# Validaciones por condición (`if i < len(...)`) para evitar errores de índice si las listas tienen tamaños diferentes.
# Reutilización de código invocado mediante `self.intercalar()` para extender el comportamiento a múltiples listas.


# 4. CODIGO
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
        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)
        return resultado


# 5. PRUEBA / DEPURACION
# Instanciación:
# cl = CombinadorListas()
#
# Ejecución: cl.intercalar([1, 2], [3, 4])
# Paso 1: lista1 = [1, 2], lista2 = [3, 4]
# Paso 2: max_len = max(2, 2) = 2
# Paso 3: Iteración i = 0
#   - 0 < len(lista1) (2) -> resultado.append(lista1[0]) -> resultado = [1]
#   - 0 < len(lista2) (2) -> resultado.append(lista2[0]) -> resultado = [1, 3]
# Paso 4: Iteración i = 1
#   - 1 < len(lista1) (2) -> resultado.append(lista1[1]) -> resultado = [1, 3, 2]
#   - 1 < len(lista2) (2) -> resultado.append(lista2[1]) -> resultado = [1, 3, 2, 4]
# Resultado final: [1, 3, 2, 4]