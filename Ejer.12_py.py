# EJERCICIO 12 - Selector de rango con tuplas

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# pares (inicio, fin) para varios rangos
# PROCESO:
# crear rangos como tuplas, unir sin duplicados
# SALIDA:
# lista de elementos únicos
# Ejemplo de entrada:
# sr = SelectorRango()
# sr.elementos_en_multiples_rangos((1,3), (2,4))
# Salida esperada:
# [1, 2, 3, 4]

# 2. BOSQUEJO
# Instancia: sr = SelectorRango()
#
# Método crear_rango(1, 3):
#   - Generar rango de 1 a 3 inclusive: tuple(range(1, 3 + 1)) -> (1, 2, 3)
#
# Método elementos_en_multiples_rangos((1, 3), (2, 4)):
#   - Recibir tuplas mediante *rangos: rangos = ((1, 3), (2, 4))
#   - Inicializar un conjunto para eliminar duplicados: conjunto_unicos = set()
#   - Para la primera tupla (1, 3):
#       Llamar a crear_rango(1, 3) -> retorna (1, 2, 3)
#       Agregar al conjunto -> conjunto_unicos = {1, 2, 3}
#   - Para la segunda tupla (2, 4):
#       Llamar a crear_rango(2, 4) -> retorna (2, 3, 4)
#       Agregar al conjunto -> conjunto_unicos = {1, 2, 3, 4}
#   - Convertir conjunto a lista ordenada -> list(sorted(conjunto_unicos)) -> [1, 2, 3, 4]

# 3. PATRON
# Generación de secuencias numéricas con range(inicio, fin + 1) convertidas a tupla.
# Uso de conjuntos (set) para garantizar la unicidad de los elementos combinados.
# Empaquetado de argumentos con *rangos para procesar múltiples tuplas.


# 4. CODIGO
class SelectorRango:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        conjunto_unicos = set()
        for r in rangos:
            inicio, fin = r
            tupla_rango = self.crear_rango(inicio, fin)
            conjunto_unicos.update(tupla_rango)
        return list(sorted(conjunto_unicos))


# 5. PRUEBA / DEPURACION
# Instanciación:
# sr = SelectorRango()
#
# Ejecución: sr.elementos_en_multiples_rangos((1, 3), (2, 4))
# Paso 1: rangos = ((1, 3), (2, 4))
# Paso 2: r = (1, 3) -> inicio = 1, fin = 3
#   - self.crear_rango(1, 3) retora tuple(range(1, 4)) -> (1, 2, 3)
#   - conjunto_unicos.update((1, 2, 3)) -> conjunto_unicos = {1, 2, 3}
# Paso 3: r = (2, 4) -> inicio = 2, fin = 4
#   - self.crear_rango(2, 4) retorna tuple(range(2, 5)) -> (2, 3, 4)
#   - conjunto_unicos.update((2, 3, 4)) -> conjunto_unicos = {1, 2, 3, 4}
# Paso 4: list(sorted({1, 2, 3, 4}))
# Resultado final: [1, 2, 3, 4]