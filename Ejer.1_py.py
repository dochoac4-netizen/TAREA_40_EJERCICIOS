# EJERCICIO 1 - Validador de notas con promedio

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# notas individuales o en lotes (*args)
# PROCESO:
# validar cada nota (0-100), guardar en lista interna, calcular promedio
# SALIDA:
# True/False (en validar_nota), lista de válidas (en cargar_notas), promedio (en promedio)
# Ejemplo de entrada:
# c = Calificador()
# c.cargar_notas(85, 92, 110, 78, -5, 88)
# c.promedio()
# Salida esperada:
# [85, 92, 78, 88]
# 85.75


# 2. BOSQUEJO
# Instancia: c = Calificador() -> self.notas = []
#
# Método validar_nota(nota):
#   - Retornar True si 0 <= nota <= 100, False en caso contrario.
#
# Método cargar_notas(85, 92, 110, 78, -5, 88):
#   - Recorrer *args:
#       * 85  -> validar_nota(85)  es True  -> agregar a self.notas
#       * 92  -> validar_nota(92)  es True  -> agregar a self.notas
#       * 110 -> validar_nota(110) es False -> ignorar
#       * 78  -> validar_nota(78)  es True  -> agregar a self.notas
#       * -5  -> validar_nota(-5)  es False -> ignorar
#       * 88  -> validar_nota(88)  es True  -> agregar a self.notas
#   - Retornar lista interna self.notas -> [85, 92, 78, 88]
#
# Método promedio():
#   - Sumar notas de la lista y dividir por la cantidad: sum(self.notas) / len(self.notas)
#   - sum([85, 92, 78, 88]) / 4 = 343 / 4 = 85.75


# 3. PATRON
# Encapsulamiento con atributo de lista interna (`self.notas`).
# Empaquetado de parámetros variables (`*args`).
# Reutilización de métodos internos (`self.validar_nota()`) dentro de otros métodos de la clase.


# 4. CODIGO
class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)


# 5. PRUEBA / DEPURACION
# Instanciación:
# c = Calificador() -> self.notas = []
#
# Ejecución 1: c.cargar_notas(85, 92, 110, 78, -5, 88)
# - Evaluando 85  -> 0 <= 85 <= 100  (True)  -> self.notas = [85]
# - Evaluando 92  -> 0 <= 92 <= 100  (True)  -> self.notas = [85, 92]
# - Evaluando 110 -> 0 <= 110 <= 100 (False) -> Ignorado
# - Evaluando 78  -> 0 <= 78 <= 100  (True)  -> self.notas = [85, 92, 78]
# - Evaluando -5  -> 0 <= -5 <= 100  (False) -> Ignorado
# - Evaluando 88  -> 0 <= 88 <= 100  (True)  -> self.notas = [85, 92, 78, 88]
# Retorna: [85, 92, 78, 88]
#
# Ejecución 2: c.promedio()
# - sum([85, 92, 78, 88]) = 343
# - len([85, 92, 78, 88]) = 4
# - 343 / 4 = 85.75
# Retorna: 85.75