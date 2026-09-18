# EJERCICIO 11 - CONTADOR DE FRECUENCIA

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# elementos individuales o en lote
# PROCESO:
# guardar en diccionario, contar, encontrar máximo
# SALIDA:
# elemento más frecuente y su conteo
# Ejemplo de entrada:
# cf = ContadorFrecuencia()
# cf.agregar_elemento("a")
# cf.agregar_elemento("b")
# cf.agregar_elemento("a")
# cf.elemento_mas_frecuente()
# Salida esperada:
# "a"

# 2. BOSQUEJO
# Instancia: self.frecuencias = {}
#
# Paso 1: cf.agregar_elemento("a")
#   - "a" es individual -> self.frecuencias = {"a": 1}
# Paso 2: cf.agregar_elemento("b")
#   - "b" es individual -> self.frecuencias = {"a": 1, "b": 1}
# Paso 3: cf.agregar_elemento("a")
#   - "a" es individual -> self.frecuencias = {"a": 2, "b": 1}
# Paso 4: cf.agregar_elemento(["c", "a"]) (Ejemplo en lote)
#   - Se descompone la lista -> "c" suma 1, "a" suma 1 -> self.frecuencias = {"a": 3, "b": 1, "c": 1}
#
# cf.elemento_mas_frecuente():
#   Comparar valores en self.frecuencias -> Maximo es 3 (asociado a "a")
#   Retorna "a"

# 3. PATRON
# Uso de *args para soporte de múltiples argumentos.
# Verificación de tipos mediante isinstance(item, (list, tuple)) para procesar lotes.
# Diccionario contador con el método .get(clave, valor_por_defecto).
# Búsqueda de clave con valor máximo usando max(dict, key=dict.get).


# 4. CODIGO
class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, *args):
        for item in args:
            if isinstance(item, (list, tuple)):
                for elem in item:
                    self.frecuencias[elem] = self.frecuencias.get(elem, 0) + 1
            else:
                self.frecuencias[item] = self.frecuencias.get(item, 0) + 1

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


# 5. PRUEBA / DEPURACION
# Instanciación:
# cf = ContadorFrecuencia() -> self.frecuencias = {}
#
# Paso 1: cf.agregar_elemento("a")
#   - item = "a" (no es lista/tupla)
#   - self.frecuencias["a"] = get("a", 0) + 1 = 1
#
# Paso 2: cf.agregar_elemento("b")
#   - item = "b" (no es lista/tupla)
#   - self.frecuencias["b"] = get("b", 0) + 1 = 1
#
# Paso 3: cf.agregar_elemento("a")
#   - item = "a" (no es lista/tupla)
#   - self.frecuencias["a"] = get("a", 1) + 1 = 2
#   - Diccionario actual: {"a": 2, "b": 1}
#
# Paso 4: cf.elemento_mas_frecuente()
#   - max() compara los valores: "a" -> 2, "b" -> 1.
# Resultado final:
# "a"