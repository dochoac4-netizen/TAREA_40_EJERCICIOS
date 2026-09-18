# EJERCICIO DE PRÁCTICA - INVERSOR DE SECUENCIAS

# 1. ENTENDER EL PROBLEMA
# ENTRADA: lista o varias listas
# PROCESO: invertir manualmente, guardar en diccionario
# SALIDA: lista invertida o diccionario
# EJEMPLO DE ENTRADA:
# inv = InversorSecuencia()
# inv.invertir_lista([4, 5, 6])
# SALIDA ESPERADA: [6, 5, 4]


# 2. BOSQUEJO
# Invertir [4, 5, 6]:
#   6 -> [6]
#   5 -> [6, 5]
#   4 -> [6, 5, 4]
#
# Múltiples listas ([10, 20], [7, 8, 9]):
#   [10, 20]  -> clave: (10, 20)  | valor: [20, 10]
#   [7, 8, 9] -> clave: (7, 8, 9) | valor: [9, 8, 7]
#   Diccionario: {(10, 20): [20, 10], (7, 8, 9): [9, 8, 7]}


# 3. PATRON
# Colecciones: listas y diccionarios con tuplas como claves


# 4. CODIGO
class InversorSecuencia:

    def invertir_lista(self, lista):
        nueva_lista = []
        for i in range(len(lista) - 1, -1, -1):
            nueva_lista.append(lista[i])
        return nueva_lista

    def invertir_multiples(self, *listas):
        diccionario = {}
        for l in listas:
            clave = tuple(l)
            diccionario[clave] = self.invertir_lista(l)
        return diccionario


# 5. PRUEBA / DEPURACION
# inv = InversorSecuencia()

# invertir_lista([4, 5, 6])
# len = 3 -> índices: 2, 1, 0
# i = 2 -> lista[2] = 6 -> [6]
# i = 1 -> lista[1] = 5 -> [6, 5]
# i = 0 -> lista[0] = 4 -> [6, 5, 4] -> Retorna [6, 5, 4]

# invertir_multiples([10, 20], [7, 8, 9])
# diccionario = {}
# 1. l = [10, 20] -> tuple = (10, 20) -> invertir_lista([10, 20]) = [20, 10] -> {(10, 20): [20, 10]}
# 2. l = [7, 8, 9] -> tuple = (7, 8, 9) -> invertir_lista([7, 8, 9]) = [9, 8, 7] -> {(10, 20): [20, 10], (7, 8, 9): [9, 8, 7]}
# Retorna: {(10, 20): [20, 10], (7, 8, 9): [9, 8, 7]}