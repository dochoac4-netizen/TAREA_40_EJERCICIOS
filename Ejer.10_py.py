# EJERCICIO 10 - Gestor de tareas con prioridad

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# descripciones y prioridades
# PROCESO:
# guardar tuplas, filtrar por prioridad, eliminar
# SALIDA:
# tareas filtradas
# Ejemplo de entrada:
# t = Tareas()
# t.agregar_tarea("Estudiar", "alta")
# t.agregar_tarea("Leer", "baja")
# t.tareas_prioritarias()
# Salida esperada:
# [("Estudiar", "alta")]


# 2. BOSQUEJO
# Instancia: t = Tareas() -> self.lista_tareas = []
#
# Método agregar_tarea("Estudiar", "alta"):
#   - Crear tupla ("Estudiar", "alta") y añadirla con .append()
#
# Método tareas_prioritarias():
#   - Recorrer self.lista_tareas y filtrar solo las tuplas donde prioridad == "alta"
#   - Retornar [("Estudiar", "alta")]
#
# Método eliminar_completada("Estudiar"):
#   - Reconstruir la lista excluyendo la tupla cuya descripción coincida con "Estudiar"


# 3. PATRON
# Uso de listas de tuplas `[(descripcion, prioridad)]` como colecciones inmutables.
# Desempaquetado de tuplas durante la iteración (`for descripcion, prioridad in self.lista_tareas`).
# Filtrado y eliminación de elementos mediante comprensión de listas o reconstrucción de listas.


# 4. CODIGO
class Tareas:

    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [
            (desc, prio)
            for desc, prio in self.lista_tareas
            if prio.lower() == "alta"
        ]

    def eliminar_completada(self, descripcion):
        self.lista_tareas = [
            (desc, prio)
            for desc, prio in self.lista_tareas
            if desc != descripcion
        ]


# 5. PRUEBA / DEPURACION
# Instanciación:
# t = Tareas() -> self.lista_tareas = []
#
# Paso 1: t.agregar_tarea("Estudiar", "alta")
#   -> self.lista_tareas = [("Estudiar", "alta")]
#
# Paso 2: t.agregar_tarea("Leer", "baja")
#   -> self.lista_tareas = [("Estudiar", "alta"), ("Leer", "baja")]
#
# Paso 3: t.tareas_prioritarias()
#   - Tupla 1 ("Estudiar", "alta"): "alta" == "alta" -> True
#   - Tupla 2 ("Leer", "baja"): "baja" == "alta" -> False
# Retorna: [("Estudiar", "alta")]