# EJERCICIO DE PRÁCTICA - CONTROL DE EDADES

# 1. ENTENDER EL PROBLEMA
# ENTRADA: edades (*args)
# PROCESO: filtrar mayores (>=18), guardar en lista y promediar
# SALIDA: lista de válidas, promedio
# Entrada: control.cargar_edades(15, 20, 18, 12, 25)
# Salida esperada: [20, 18, 25] y 21.0


# 2. BOSQUEJO
# self.edades = []
# 15 < 18 -> descarta
# 20 >= 18 -> [20]
# 18 >= 18 -> [20, 18]
# 12 < 18 -> descarta
# 25 >= 18 -> [20, 18, 25]
# Promedio: (20 + 18 + 25) / 3 = 21.0


# 3. PATRON
# Clases con POO, filtro condicional (if), acumulación en lista y sum()/len() para el promedio.


# 4. CODIGO
class ControlEdad:

    def __init__(self):
        self.edades = []

    def es_mayor(self, edad):
        return edad >= 18

    def cargar_edades(self, *args):
        for edad in args:
            if self.es_mayor(edad):
                self.edades.append(edad)
        return self.edades

    def edad_promedio(self):
        if not self.edades:
            return 0
        return sum(self.edades) / len(self.edades)


# 5. PRUEBA / DEPURACION
# control = ControlEdad() -> self.edades = []
# cargar_edades(15, 20, 18, 12, 25)
# 15 -> False
# 20 -> True -> [20]
# 18 -> True -> [20, 18]
# 12 -> False
# 25 -> True -> [20, 18, 25] -> Retorna [20, 18, 25]
# edad_promedio() -> 63 / 3 = 21.0 -> Retorna 21.0
