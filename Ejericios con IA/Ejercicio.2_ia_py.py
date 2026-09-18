# EJERCICIO A - FILTRO DE NOTAS APROBADAS

# 1. ENTENDER EL PROBLEMA
# ENTRADA: notas numéricas (*args)
# PROCESO: filtrar aprobadas (>= 7), guardar en lista y promediar
# SALIDA: lista de aprobadas, promedio
# Entrada: gestor.cargar_notas(5, 8, 7, 4, 10)
# Salida esperada: [8, 7, 10] y 8.33


# 2. BOSQUEJO
# self.notas = []
# 5 < 7 -> descarta
# 8 >= 7 -> [8]
# 7 >= 7 -> [8, 7]
# 4 < 7 -> descarta
# 10 >= 7 -> [8, 7, 10]
# Promedio: (8 + 7 + 10) / 3 = 8.33


# 3. PATRON
# Clases con POO, filtro condicional (if), acumulación en lista y sum()/len() para promedio.


# 4. CODIGO
class GestorNotas:

    def __init__(self):
        self.notas = []

    def es_aprobada(self, nota):
        return nota >= 7

    def cargar_notas(self, *args):
        for nota in args:
            if self.es_aprobada(nota):
                self.notas.append(nota)
        return self.notas

    def nota_promedio(self):
        if not self.notas:
            return 0
        return round(sum(self.notas) / len(self.notas), 2)


# 5. PRUEBA / DEPURACION
# g = GestorNotas() -> self.notas = []
# cargar_notas(5, 8, 7, 4, 10)
# 5 -> False
# 8 -> True -> [8]
# 7 -> True -> [8, 7]
# 4 -> False
# 10 -> True -> [8, 7, 10] -> Retorna [8, 7, 10]
# nota_promedio() -> 25 / 3 = 8.33 -> Retorna 8.33