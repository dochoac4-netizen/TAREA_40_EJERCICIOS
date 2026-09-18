# EJERCICIO 17 - Grupo de edades

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# edades en lote (*edades)
# PROCESO:
# clasificar con if/elif, agrupar en diccionario
# SALIDA:
# diccionario agrupado, promedio
# Ejemplo de entrada:
# ae = AgrupadorEdades()
# ae.agrupar_por_categoria(5, 15, 30, 70)
# Salida esperada:
# {'niño': [5], 'adolescente': [15], 'adulto': [30], 'mayor': [70]}

# 2. BOSQUEJO
# Instancia: ae = AgrupadorEdades() -> self.grupos = {'niño': [], 'adolescente': [], 'adulto': [], 'mayor': []}
#
# Método clasificar_edad(edad):
#   - Si edad < 12 -> "niño"
#   - Si 12 <= edad < 18 -> "adolescente"
#   - Si 18 <= edad < 65 -> "adulto"
#   - Si edad >= 65 -> "mayor"
#
# Método agrupar_por_categoria(5, 15, 30, 70):
#   - Recorrer *edades:
#       * 5  -> clasificar_edad(5)  = "niño"        -> agregar a self.grupos['niño']
#       * 15 -> clasificar_edad(15) = "adolescente" -> agregar a self.grupos['adolescente']
#       * 30 -> clasificar_edad(30) = "adulto"      -> agregar a self.grupos['adulto']
#       * 70 -> clasificar_edad(70) = "mayor"       -> agregar a self.grupos['mayor']
#   - Retornar el diccionario self.grupos
#
# Método edad_promedio_categoria("adulto"):
#   - Obtener lista de 'adulto' -> [30]
#   - Sumar valores y dividir por total -> sum([30]) / len([30]) = 30.0

# 3. PATRON
# Clasificación condicional utilizando la estructura de control `if/elif/else`.
# Agrupamiento de datos dentro de una estructura anidada de Diccionario de Listas `{categoria: [lista_edades]}`.
# Cálculo estadístico simple (promedio) validando el caso de lista vacía para prevenir división por cero (`ZeroDivisionError`).


# 4. CODIGO
class AgrupadorEdades:

    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": [],
        }

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        for edad in edades:
            cat = self.clasificar_edad(edad)
            self.grupos[cat].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.grupos or not self.grupos[categoria]:
            return 0.0
        lista_edades = self.grupos[categoria]
        return sum(lista_edades) / len(lista_edades)


# 5. PRUEBA / DEPURACION
# Instanciación:
# ae = AgrupadorEdades() -> self.grupos = {'niño': [], 'adolescente': [], 'adulto': [], 'mayor': []}
#
# Ejecución: ae.agrupar_por_categoria(5, 15, 30, 70)
# Paso 1: edad = 5  -> clasificar_edad(5)  -> "niño"        -> self.grupos['niño'].append(5)
# Paso 2: edad = 15 -> clasificar_edad(15) -> "adolescente" -> self.grupos['adolescente'].append(15)
# Paso 3: edad = 30 -> clasificar_edad(30) -> "adulto"      -> self.grupos['adulto'].append(30)
# Paso 4: edad = 70 -> clasificar_edad(70) -> "mayor"       -> self.grupos['mayor'].append(70)
#
# Resultado final devuelto:
# {'niño': [5], 'adolescente': [15], 'adulto': [30], 'mayor': [70]}