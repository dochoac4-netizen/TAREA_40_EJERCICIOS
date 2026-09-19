# Ej. 14 MEDIO  Mapeo de estudiantes a notas

# Clase RegistroNotas que: (1) tenga método registrar(estudiante, nota) que guarde en un diccionario; (2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; (3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.

# ENTRADA
# estudiante -> nota

# PROCESO
# guardar diccionario, iterar con items(), comparar

# SALIDA
# listas filtradas, tupla (nombre, nota)

# EJEMPLO DE ENTRADA
# rn = RegistroNotas()
# rn.registrar("Ana", 95)
# rn.registrar("Bob", 70)
# rn.mejor_estudiante()

# SALIDA ESPERADA
# ("Ana", 95)

# Colecciones: diccionario.items() para iterar clave-valor


class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados

    def mejor_estudiante(self):
        if not self.notas:
            return None

        mejor_nombre = None
        mejor_nota = -1

        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)

# DEPURACIÓN / PRUEBA DE ESCRITORIO
# rn = RegistroNotas() -> self.notas = {}

# 1. Probar registrar:
# rn.registrar("Ana", 95) -> self.notas["Ana"] = 95
# rn.registrar("Bob", 70) -> self.notas["Bob"] = 70
# Estado de self.notas: {"Ana": 95, "Bob": 70}

# 2. Probar estudiantes_aprobados:
# rn.estudiantes_aprobados(80)
# -> "Ana": 95 >= 80 -> aprobados.append("Ana")
# -> "Bob": 70 >= 80 -> False
# -> Retorna: ["Ana"]

# 3. Probar mejor_estudiante:
# rn.mejor_estudiante()
# -> Inicializa: mejor_nombre = None, mejor_nota = -1
# -> Iteración 1: "Ana", 95 -> 95 > -1 -> mejor_nombre = "Ana", mejor_nota = 95
# -> Iteración 2: "Bob", 70 -> 70 > 95 -> False
# -> Retorna tupla: ("Ana", 95)