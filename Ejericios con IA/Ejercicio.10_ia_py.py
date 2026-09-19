# Ej. 10 MEDIO  Gestor de tareas con prioridad

# Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad); (2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta; (3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.

# ENTRADA
# descripciones y prioridades

# PROCESO
# guardar tuplas, filtrar por prioridad, eliminar

# SALIDA
# tareas filtradas

# EJEMPLO DE ENTRADA
# t = Tareas()
# t.agregar_tarea("Estudiar", "alta")
# t.agregar_tarea("Leer", "baja")
# t.tareas_prioritarias()

# SALIDA ESPERADA
# [("Estudiar", "alta")]

# Colecciones: lista de tuplas (inmutables, ordenadas)


class Tareas:

    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        prioritarias = []
        for descripcion, prioridad in self.lista_tareas:
            if prioridad == "alta":
                prioritarias.append((descripcion, prioridad))
        return prioritarias

    def eliminar_completada(self, descripcion):
        self.lista_tareas = [
            tarea for tarea in self.lista_tareas if tarea[0] != descripcion
        ]


# DEPURACIÓN / PRUEBA DE ESCRITORIO
# t = Tareas() -> self.lista_tareas = []

# 1. Probar agregar_tarea:
# t.agregar_tarea("Estudiar", "alta") -> append(("Estudiar", "alta"))
# t.agregar_tarea("Leer", "baja")     -> append(("Leer", "baja"))
# Estado de self.lista_tareas: [("Estudiar", "alta"), ("Leer", "baja")]

# 2. Probar tareas_prioritarias:
# t.tareas_prioritarias()
# -> prioritarias = []
# -> Iteración 1: ("Estudiar", "alta") -> prioridad == "alta" (True)  -> append(("Estudiar", "alta"))
# -> Iteración 2: ("Leer", "baja")     -> prioridad == "alta" (False) -> se omite
# -> Retorna: [("Estudiar", "alta")]

# 3. Probar eliminar_completada:
# t.eliminar_completada("Leer")
# -> Filtra conservando tareas cuyo elemento index 0 != "Leer"
# -> Estado final de self.lista_tareas: [("Estudiar", "alta")]