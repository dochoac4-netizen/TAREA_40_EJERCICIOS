# EJERCICIO DE PRÁCTICA - ESTADÍSTICAS DE CALIFICACIONES

# 1. ENTENDER EL PROBLEMA
# ENTRADA: calificaciones individuales o en lote
# PROCESO: guardar, calcular mín, máx, promedio
# SALIDA: valores estadísticos
# EJEMPLO DE ENTRADA:
# gc = GestorCalificaciones()
# gc.registrar_multiples(14, 18, 12, 16)
# gc.promedio()
# SALIDA ESPERADA:
# 15.0


# 2. BOSQUEJO
# Registrar (14, 18, 12, 16):
#   self.notas = [14, 18, 12, 16]
#
# Cálculos:
#   minima(): min([14, 18, 12, 16]) -> 12
#   maxima(): max([14, 18, 12, 16]) -> 18
#   promedio(): sum([14, 18, 12, 16]) / len([14, 18, 12, 16])
#              -> 60 / 4 -> 15.0


# 3. PATRON
# Colecciones: lista de números + funciones built-in min/max


# 4. CODIGO
class GestorCalificaciones:

    def __init__(self):
        self.notas = []

    def registrar_calificacion(self, nota):
        self.notas.append(nota)

    def registrar_multiples(self, *notas):
        for nota in notas:
            self.registrar_calificacion(nota)

    def minima(self):
        if not self.notas:
            return 0
        return min(self.notas)

    def maxima(self):
        if not self.notas:
            return 0
        return max(self.notas)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)


# 5. PRUEBA / DEPURACION
# gc = GestorCalificaciones() -> self.notas = []

# registrar_multiples(14, 18, 12, 16)
# nota = 14 -> registrar_calificacion(14) -> notas = [14]
# nota = 18 -> registrar_calificacion(18) -> notas = [14, 18]
# nota = 12 -> registrar_calificacion(12) -> notas = [14, 18, 12]
# nota = 16 -> registrar_calificacion(16) -> notas = [14, 18, 12, 16]

# promedio()
# sum(notas) = 60
# len(notas) = 4
# 60 / 4 -> Retorna: 15.0