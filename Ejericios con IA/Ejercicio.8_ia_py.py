# EJERCICIO DE PRÁCTICA - ASIGNADOR DE PROYECTOS

# 1. ENTENDER EL PROBLEMA
# ENTRADA: nombres de proyectos y empleados
# PROCESO: crear estructura proyecto->[empleados], contar, comparar
# SALIDA: proyecto con mayor cantidad
# EJEMPLO DE ENTRADA:
# gestor = AsignadorProyectos()
# gestor.crear_proyecto("Alfa")
# gestor.agregar_empleado("Alfa", "Carlos")
# gestor.proyecto_mayor_integrantes()
# SALIDA ESPERADA:
# "Alfa"


# 2. BOSQUEJO
# Crear proyecto "Alfa":
#   self.proyectos = {"Alfa": []}
#
# Agregar empleado:
#   "Alfa": ["Carlos"] -> len = 1
#
# Proyecto mayor:
#   len("Alfa") = 1 -> Proyecto mayor: "Alfa"


# 3. PATRON
# Colecciones: diccionario de listas (estructura anidada)


# 4. CODIGO
class AsignadorProyectos:

    def __init__(self):
        self.proyectos = {}

    def crear_proyecto(self, nombre_proyecto):
        self.proyectos[nombre_proyecto] = []

    def agregar_empleado(self, nombre_proyecto, empleado):
        if nombre_proyecto in self.proyectos:
            self.proyectos[nombre_proyecto].append(empleado)

    def proyecto_mayor_integrantes(self):
        if not self.proyectos:
            return None

        mayor_proyecto = None
        max_integrantes = -1

        for proyecto, lista_empleados in self.proyectos.items():
            if len(lista_empleados) > max_integrantes:
                max_integrantes = len(lista_empleados)
                mayor_proyecto = proyecto

        return mayor_proyecto

# 5. PRUEBA / DEPURACION
# gestor = AsignadorProyectos() -> self.proyectos = {}

# crear_proyecto("Alfa") -> self.proyectos = {"Alfa": []}
# agregar_empleado("Alfa", "Carlos") -> self.proyectos = {"Alfa": ["Carlos"]}

# proyecto_mayor_integrantes()
# 1. proyecto = "Alfa", len = 1 -> 1 > -1 -> mayor_proyecto = "Alfa", max_integrantes = 1
# Retorna: "Alfa"