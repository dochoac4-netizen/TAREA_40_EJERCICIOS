# EJERCICIO 20 - Analizador de patrones en textos

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# texto y patrón de búsqueda
# PROCESO:
# split(), filtrar con .startswith(), agrupar por longitud, eliminar duplicados
# SALIDA:
# listas, diccionario, conjunto
# Ejemplo de entrada:
# ap = AnalizadorPatrones()
# ap.agrupar_por_longitud("el gato está aquí")
# Salida esperada:
# {2: ['el'], 4: ['gato'], 4: ['está'], 4: ['aquí']}  (agrupado por longitud len(palabra))

# 2. BOSQUEJO
# Instancia: ap = AnalizadorPatrones() -> self.historial_palabras = set()
#
# Método encontrar_palabras("el gato está aquí", "ga"):
#   - Separar texto: palabras = texto.split()
#   - Coincidencias: [p for p in palabras if p.startswith("ga")] -> ["gato"]
#   - Guardar palabras procesadas en self.historial_palabras (set)
#   - Retornar ["gato"]
#
# Método agrupar_por_longitud("el gato está aquí"):
#   - Separar texto: ["el", "gato", "está", "aquí"]
#   - Agrupar en diccionario por len():
#       * "el"   -> len=2 -> {2: ["el"]}
#       * "gato" -> len=4 -> {2: ["el"], 4: ["gato"]}
#       * "está" -> len=4 -> {2: ["el"], 4: ["gato", "está"]}
#       * "aquí" -> len=4 -> {2: ["el"], 4: ["gato", "está", "aquí"]}
#   - Guardar palabras procesadas en self.historial_palabras
#   - Retornar diccionario
#
# Método palabras_unicas():
#   - Retornar self.historial_palabras (que al ser set no tiene duplicados)

# 3. PATRON
# Procesamiento de strings mediante `.split()` para tokenizar y `.startswith()` para coincidencia de prefijos.
# Agrupamiento dinámico con claves numéricas (longitudes) en un diccionario `{int: list}`.
# Eliminación de elementos duplicados utilizando un Conjunto (`set()`) mediante el método `.update()`.


# 4. CODIGO
class AnalizadorPatrones:

    def __init__(self):
        self.historial_palabras = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        coincidencias = [p for p in palabras if p.startswith(patron)]
        self.historial_palabras.update(palabras)
        return coincidencias

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        agrupadas = {}

        for p in palabras:
            longitud = len(p)
            if longitud not in agrupadas:
                agrupadas[longitud] = []
            agrupadas[longitud].append(p)

        self.historial_palabras.update(palabras)
        return agrupadas

    def palabras_unicas(self):
        return self.historial_palabras


# 5. PRUEBA / DEPURACION
# Instanciación:
# ap = AnalizadorPatrones() -> self.historial_palabras = set()
#
# Ejecución: ap.agrupar_por_longitud("el gato está aquí")
# Paso 1: texto.split() -> ["el", "gato", "está", "aquí"]
# Paso 2: "el"   -> len("el") = 2   -> agrupadas[2] = ["el"]
# Paso 3: "gato" -> len("gato") = 4 -> agrupadas[4] = ["gato"]
# Paso 4: "está" -> len("está") = 4 -> agrupadas[4] = ["gato", "está"]
# Paso 5: "aquí" -> len("aquí") = 4 -> agrupadas[4] = ["gato", "está", "aquí"]
# Paso 6: self.historial_palabras.update(...) -> {'el', 'gato', 'está', 'aquí'}
#
# Resultado retornado: {2: ['el'], 4: ['gato', 'está', 'aquí']}