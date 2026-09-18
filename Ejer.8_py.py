# EJERCICIO 8 - Asignador de equipos

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# nombres de equipos y jugadores
# PROCESO:
# crear estructura equipo->[jugadores], contar, comparar
# SALIDA:
# equipo con mayor cantidad
# Ejemplo de entrada:
# eq = Equipos()
# eq.crear_equipo("A")
# eq.agregar_jugador("A", "Juan")
# eq.agregar_jugador("A", "Pedro")
# Salida esperada:
# "A"


# 2. BOSQUEJO
# Instancia: eq = Equipos() -> self.equipos = {}
#
# Método crear_equipo("A"):
#   - Insertar clave con lista vacía: self.equipos["A"] = []
#
# Método agregar_jugador("A", "Juan"):
#   - Si el equipo existe en el diccionario, agregar "Juan" a la lista:
#     self.equipos["A"].append("Juan")
#
# Método equipo_mayor_integrantes():
#   - Recorrer self.equipos.items() para buscar la clave cuyo len(lista) sea el máximo.
#   - Retornar el nombre del equipo ("A").


# 3. PATRON
# Diccionario de listas como estructura anidada `{nombre_equipo: [jugadores]}`.
# Modificación de listas contenidas en un diccionario vía `.append()`.
# Algoritmo de búsqueda de máximo utilizando `len()` en las listas internas.


# 4. CODIGO
class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        return max(
            self.equipos,
            key=lambda nombre: len(self.equipos[nombre])
        )


# 5. PRUEBA / DEPURACION
# Instanciación:
# eq = Equipos() -> self.equipos = {}
#
# Paso 1: eq.crear_equipo("A")
#   -> self.equipos = {"A": []}
#
# Paso 2: eq.agregar_jugador("A", "Juan")
#   -> self.equipos["A"].append("Juan") -> {"A": ["Juan"]}
#
# Paso 3: eq.agregar_jugador("A", "Pedro")
#   -> self.equipos["A"].append("Pedro") -> {"A": ["Juan", "Pedro"]}
#
# Paso 4: eq.equipo_mayor_integrantes()
#   - Mide tamaño de "A": len(["Juan", "Pedro"]) = 2
#   - Es el máximo de la estructura.
# Retorna: "A"