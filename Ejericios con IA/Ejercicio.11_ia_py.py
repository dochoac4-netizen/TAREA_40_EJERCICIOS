# Ej. 14 MEDIO  Filtro y mapeador de diccionarios

# Clase FiltroDiccionario que: (1) tenga método filtrar_mayores(diccionario, umbral) que retorne un nuevo diccionario solo con las claves cuyo valor sea estrictamente mayor al umbral; (2) tenga método procesar_multiples_diccionarios(umbral, *diccionarios) que combine todos los diccionarios filtrados en uno solo.

# ENTRADA
# uno o varios diccionarios y un valor umbral numérico

# PROCESO
# iterar claves y valores con bucles/items, evaluar condición, combinar diccionarios

# SALIDA
# diccionario filtrado o diccionario combinado filtrado

# EJEMPLO DE ENTRADA
# fd = FiltroDiccionario()
# fd.filtrar_mayores({"a": 10, "b": 5, "c": 20}, 8)

# SALIDA ESPERADA
# {"a": 10, "c": 20}

# Colecciones: iteración de diccionarios (.items()) y empaquetado *args


class FiltroDiccionario:

    def filtrar_mayores(self, diccionario, umbral):
        resultado = {}
        for clave, valor in diccionario.items():
            if valor > umbral:
                resultado[clave] = valor
        return resultado

    def procesar_multiples_diccionarios(self, umbral, *diccionarios):
        combinado = {}
        for d in diccionarios:
            filtrado = self.filtrar_mayores(d, umbral)
            for clave, valor in filtrado.items():
                combinado[clave] = valor
        return combinado


# DEPURACIÓN / PRUEBA DE ESCRITORIO
# fd = FiltroDiccionario()

# 1. Probar filtrar_mayores:
# fd.filtrar_mayores({"a": 10, "b": 5, "c": 20}, 8)
# -> Iteración 1: "a", 10 -> 10 > 8 (True) -> resultado["a"] = 10
# -> Iteración 2: "b", 5  -> 5 > 8 (False) -> se omite
# -> Iteración 3: "c", 20 -> 20 > 8 (True) -> resultado["c"] = 20
# -> Retorna: {"a": 10, "c": 20}

# 2. Probar procesar_multiples_diccionarios:
# fd.procesar_multiples_diccionarios(8, {"a": 10, "b": 5}, {"c": 20, "d": 2})
# -> d1 = {"a": 10, "b": 5} -> filtrar_mayores(d1, 8) -> {"a": 10}
# -> d2 = {"c": 20, "d": 2} -> filtrar_mayores(d2, 8) -> {"c": 20}
# -> Agrega ambos al diccionario combinado
# -> Retorna: {"a": 10, "c": 20}
