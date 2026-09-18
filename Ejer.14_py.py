# EJERCICIO 14 - Mapeo de estudiantes a notas

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# estudiante -> nota
# PROCESO:
# guardar diccionario, iterar con items(), comparar
# SALIDA:
# listas filtradas, tupla (nombre, nota)
# Ejemplo de entrada:
# rn = RegistroNotas()
# rn.registrar("Ana", 95)
# rn.registrar("Bob", 70)
# rn.mejor_estudiante()
# Salida esperada:
# ("Ana", 95)

# 2. BOSQUEJO
# Instancia: self.registros = {}
#
# Paso 1: rn.registrar("Ana", 95)
#   - Asignar clave-valor -> self.registros["Ana"] = 95
# Paso 2: rn.registrar("Bob", 70)
#   - Asignar clave-valor -> self.registros["Bob"] = 70
#   - Diccionario actual: {"Ana": 95, "Bob": 70}
#
# Método estudiantes_aprobados(75):
#   - Iterar con items(): ("Ana", 95) y ("Bob", 70)
#   - Filtrar donde nota >= 75 -> ["Ana"]
#
# Método mejor_estudiante():
#   - Iterar con items() para encontrar el valor máximo de nota:
#       * ("Ana", 95) vs ("Bob", 70) -> Nota máxima = 95
#   - Retornar tupla con el estudiante y su nota -> ("Ana", 95)

# 3. PATRON
# Uso de diccionarios para almacenamiento asociativo clave-valor (`estudiante: nota`).
# Iteración sobre pares clave-valor usando `.items()`.
# Filtrado de elementos con list comprenhension y búsqueda de máximos condicionales.


# 4. CODIGO
class RegistroNotas:

    def __init__(self):
        self.registros = {}

    def registrar(self, estudiante, nota):
        self.registros[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.registros.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados

    def mejor_estudiante(self):
        if not self.registros:
            return None

        top_estudiante = None
        top_nota = -1

        for estudiante, nota in self.registros.items():
            if nota > top_nota:
                top_nota = nota
                top_estudiante = estudiante

        return (top_estudiante, top_nota)


# 5. PRUEBA / DEPURACION
# Instanciación:
# rn = RegistroNotas() -> self.registros = {}
#
# Paso 1: rn.registrar("Ana", 95) -> self.registros = {"Ana": 95}
# Paso 2: rn.registrar("Bob", 70) -> self.registros = {"Ana": 95, "Bob": 70}
#
# Paso 3: rn.mejor_estudiante()
#   - Iteración 1: estudiante="Ana", nota=95
#       95 > -1 -> top_estudiante="Ana", top_nota=95
#   - Iteración 2: estudiante="Bob", nota=70
#       70 no es mayor que 95 -> no cambia
#   - Retorna: ("Ana", 95)
# Resultado final: ("Ana", 95)