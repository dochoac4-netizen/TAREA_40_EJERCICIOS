# EJERCICIO 7 - Mapeador de edades

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# nombres y edades
# PROCESO:
# guardar en diccionario, filtrar, promediar
# SALIDA:
# lista filtrada, promedio
# Ejemplo de entrada:
# gp = GestorPersonas()
# gp.agregar_persona("Ana", 28)
# gp.agregar_persona("Bob", 17)
# gp.personas_mayores(18)
# Salida esperada:
# ["Ana"]


# 2. BOSQUEJO
# Instancia: gp = GestorPersonas() -> self.personas = {}
#
# Método agregar_persona("Ana", 28):
#   - Insertar par clave-valor: self.personas["Ana"] = 28
#
# Método personas_mayores(18):
#   - Recorrer el diccionario con .items(): nombre, edad
#   - Si edad >= 18: guardar nombre en lista filtrada
#   - Retornar ["Ana"]
#
# Método edad_promedio():
#   - Sumar los valores con .values() y dividir entre la cantidad de registros


# 3. PATRON
# Uso de un diccionario `{nombre: edad}` como estructura de mapeo clave-valor.
# Iteración sobre clave y valor usando el método `.items()`.
# Filtrado de elementos basado en una condición condicional (edad >= edad_minima).
# Promedio aritmético con `.values()`, `sum()` y `len()`.


# 4. CODIGO
class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        filtrados = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                filtrados.append(nombre)
        return filtrados

    def edad_promedio(self):
        if not self.personas:
            return 0.0
        edades = self.personas.values()
        return sum(edades) / len(edades)


# 5. PRUEBA / DEPURACION
# Instanciación:
# gp = GestorPersonas() -> self.personas = {}
#
# Paso 1: gp.agregar_persona("Ana", 28) -> self.personas = {"Ana": 28}
# Paso 2: gp.agregar_persona("Bob", 17) -> self.personas = {"Ana": 28, "Bob": 17}
#
# Paso 3: gp.personas_mayores(18)
# - Item "Ana": 28 -> 28 >= 18 True  -> filtrados = ["Ana"]
# - Item "Bob": 17 -> 17 >= 18 False -> filtrados = ["Ana"]
# Retorna: ["Ana"]

