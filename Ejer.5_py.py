# EJERCICIO 5 - Detector de números pares e impares

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# NÚMEROS EN LOTE (*numeros)
# PROCESO:
# clasificar pares e impares con operador %
# SALIDA:
# diccionario y tupla con cantidades
# Ejemplo de entrada:
# an = AnalizadorNumeros()
# an.separar(1, 2, 3, 4, 5)
# Salida esperada:
# {'pares': [2, 4], 'impares': [1, 3, 5]}


# 2. BOSQUEJO
# Instancia: an = AnalizadorNumeros() -> self.pares = [], self.impares = []
#
# Método es_par(numero):
#   - Evaluar si numero % 2 == 0 (retorna True o False)
#
# Método separar(1, 2, 3, 4, 5):
#   - Limpiar listas: self.pares = [], self.impares = []
#   - Recorrer *numeros usando es_par(num):
#       * Si es True -> self.pares.append(num)
#       * Si es False -> self.impares.append(num)
#   - Retornar diccionario: {'pares': self.pares, 'impares': self.impares}
#
# Método cantidad_pares_impares():
#   - Retornar tupla con cantidades: (len(self.pares), len(self.impares))


# 3. PATRON
# Clasificación con operador módulo % para determinar paridad.
# Reutilización del método de instancia `self.es_par()`.
# Almacenamiento en diccionario con claves string y valores de tipo lista.
# Retorno de tupla con conteos acumulados.


# 4. CODIGO
class AnalizadorNumeros:

    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.pares = []
        self.impares = []
        for num in numeros:
            if self.es_par(num):
                self.pares.append(num)
            else:
                self.impares.append(num)
        return {"pares": self.pares, "impares": self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


# 5. PRUEBA / DEPURACION
# Instanciación:
# an = AnalizadorNumeros() -> self.pares = [], self.impares = []
#
# Ejecución 1: an.separar(1, 2, 3, 4, 5)
# - num = 1 -> es_par(1) False -> impares = [1]
# - num = 2 -> es_par(2) True  -> pares = [2]
# - num = 3 -> es_par(3) False -> impares = [1, 3]
# - num = 4 -> es_par(4) True  -> pares = [2, 4]
# - num = 5 -> es_par(5) False -> impares = [1, 3, 5]
# Retorna: {'pares': [2, 4], 'impares': [1, 3, 5]}
#
# Ejecución 2: an.cantidad_pares_impares()
# Retorna: (2, 3)