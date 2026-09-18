# EJERCICIO 15 - Divisores de un número

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# uno o varios números
# PROCESO:
# encontrar divisores con bucles, verificar suma
# SALIDA:
# tuplas, booleano, diccionario
# Ejemplo de entrada:
# df = DivisorFinder()
# df.encontrar_divisores(12)
# Salida esperada:
# (1, 2, 3, 4, 6, 12)

# 2. BOSQUEJO
# Instancia: df = DivisorFinder()
#
# Método encontrar_divisores(12):
#   - Iterar con i desde 1 hasta 12:
#       * Si 12 % i == 0, agregar i a una lista de divisores.
#   - Divisores de 12: [1, 2, 3, 4, 6, 12]
#   - Retornar convertido a tupla: (1, 2, 3, 4, 6, 12)
#
# Método es_perfecto(6):
#   - Obtener divisores propios (excluyendo el número): [1, 2, 3]
#   - Sumar divisores: 1 + 2 + 3 = 6
#   - Comparar suma con el número: 6 == 6 -> True
#
# Método encontrar_multiples_divisores(*numeros):
#   - Recibir varios números (ej: 6, 12)
#   - Crear diccionario vacio: resultado = {}
#   - Para cada número, invocar self.encontrar_divisores(n)
#   - Guardar en diccionario: resultado[n] = tupla_divisores
#   - Retornar diccionario.

# 3. PATRON
# Verificación de divisibilidad matemática mediante el operador módulo `%`.
# Conversión de colecciones dinámicas (listas) a estructuras inmutables (tuplas).
# Construcción de mapas en diccionarios `{clave: valor}` combinando *args.


# 4. CODIGO
class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        if numero <= 0:
            return False
        divisores = self.encontrar_divisores(numero)
        divisores_propios = divisores[:-1]
        return sum(divisores_propios) == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for num in numeros:
            resultado[num] = self.encontrar_divisores(num)
        return resultado


# 5. PRUEBA / DEPURACION
# Instanciación:
# df = DivisorFinder()
#
# Ejecución: df.encontrar_divisores(12)
# Paso 1: numero = 12, divisores = []
# Paso 2: Iterar i de 1 a 12
#   - i = 1: 12 % 1 == 0 -> append(1)
#   - i = 2: 12 % 2 == 0 -> append(2)
#   - i = 3: 12 % 3 == 0 -> append(3)
#   - i = 4: 12 % 4 == 0 -> append(4)
#   - i = 6: 12 % 6 == 0 -> append(6)
#   - i = 12: 12 % 12 == 0 -> append(12)
# Paso 3: tuple([1, 2, 3, 4, 6, 12])
# Resultado final: (1, 2, 3, 4, 6, 12)