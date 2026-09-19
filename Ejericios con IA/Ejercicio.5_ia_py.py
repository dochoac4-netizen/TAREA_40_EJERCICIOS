# EJERCICIO DE PRÁCTICA - CLASIFICADOR DE EDADES (MAYORES Y MENORES)

# 1. ENTENDER EL PROBLEMA
# ENTRADA: NÚMEROS EN LOTE
# PROCESO: clasificar mayores y menores de edad con operador >= 18
# SALIDA: diccionario y tupla con cantidades
# EJEMPLO DE ENTRADA:
# ce = ControlEdad()
# ce.separar(12, 20, 15, 18, 25)
# SALIDA ESPERADA:
# {'mayores': [20, 18, 25], 'menores': [12, 15]}


# 2. BOSQUEJO
# Evaluar (12, 20, 15, 18, 25):
#   12 >= 18 -> False -> agrega a 'menores': [12]
#   20 >= 18 -> True  -> agrega a 'mayores': [20]
#   15 >= 18 -> False -> agrega a 'menores': [12, 15]
#   18 >= 18 -> True  -> agrega a 'mayores': [20, 18]
#   25 >= 18 -> True  -> agrega a 'mayores': [20, 18, 25]
# Diccionario final: {'mayores': [20, 18, 25], 'menores': [12, 15]}
# Cantidades: (len([20, 18, 25]), len([12, 15])) -> Tupla: (3, 2)


# 3. PATRON
# Colecciones: diccionario con claves string y valores list


# 4. CODIGO
class ControlEdad:

    def __init__(self):
        self.mayores = []
        self.menores = []

    def es_mayor(self, edad):
        return edad >= 18

    def separar(self, *edades):
        self.mayores = []
        self.menores = []

        for edad in edades:
            if self.es_mayor(edad):
                self.mayores.append(edad)
            else:
                self.menores.append(edad)

        return {'mayores': self.mayores, 'menores': self.menores}

    def cantidad_mayores_menores(self):
        return (len(self.mayores), len(self.menores))


# 5. PRUEBA / DEPURACION
# ce = ControlEdad()

# separar(12, 20, 15, 18, 25)
# edad = 12 -> es_mayor(12) = False -> menores = [12]
# edad = 20 -> es_mayor(20) = True  -> mayores = [20]
# edad = 15 -> es_mayor(15) = False -> menores = [12, 15]
# edad = 18 -> es_mayor(18) = True  -> mayores = [20, 18]
# edad = 25 -> es_mayor(25) = True  -> mayores = [20, 18, 25]
# Retorna: {'mayores': [20, 18, 25], 'menores': [12, 15]}

# cantidad_mayores_menores()
# len(mayores) = 3
# len(menores) = 2
# Retorna: (3, 2)