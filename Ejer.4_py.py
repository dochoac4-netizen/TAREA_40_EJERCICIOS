# EJERCICIO 4 - Inversor de secuencias

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# lista o varias listas (*listas)
# PROCESO:
# invertir manualmente usando bucles (sin reversed()), reutilizar para varias listas y guardar en diccionario
# SALIDA:
# lista invertida o diccionario {lista_original: lista_invertida}
# Ejemplo de entrada:
# inv = InversorSecuencia()
# inv.invertir_lista([1, 2, 3])
# Salida esperada:
# [3, 2, 1]


# 2. BOSQUEJO
# Instancia: inv = InversorSecuencia()
#
# Método invertir_lista([1, 2, 3]):
#   - Crear lista vacía: invertida = []
#   - Iterar hacia atrás usando un bucle:
#       for i in range(len(lista) - 1, -1, -1):
#           invertida.append(lista[i])
#   - Retornar [3, 2, 1]
#
# Método invertir_multiples([1, 2, 3], [4, 5]):
#   - Crear diccionario: resultado = {}
#   - Para cada lista en *listas:
#       * Como las listas no pueden ser claves de diccionario en Python (son mutables),
#         la pista indica usar tuplas como claves: tuple(lista)
#       * resultado[tuple(lista)] = self.invertir_lista(lista)
#   - Retornar resultado


# 3. PATRON
# Inversión manual de secuencias iterando índices en sentido inverso con `range(len - 1, -1, -1)`.
# Conversión de listas mutables a tuplas inmutables (`tuple()`) para utilizarlas válidamente como claves de un diccionario.


# 4. CODIGO
class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            clave_tupla = tuple(lista)
            resultado[clave_tupla] = self.invertir_lista(lista)
        return resultado


# 5. PRUEBA / DEPURACION
# Instanciación:
# inv = InversorSecuencia()
#
# Ejecución: inv.invertir_lista([1, 2, 3])
# - len([1, 2, 3]) = 3
# - Rango de índices: 2, 1, 0
# - i = 2 -> lista[2] = 3 -> invertida = [3]
# - i = 1 -> lista[1] = 2 -> invertida = [3, 2]
# - i = 0 -> lista[0] = 1 -> invertida = [3, 2, 1]
# Retorna: [3, 2, 1]