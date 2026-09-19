# Ej. 17 BÁSICO  Grupo de edades

# Clase AgrupadorEdades que: (1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); (2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoria: [edades]}; (3) tenga método edad_promedio_categoria(categoria).

# ENTRADA
# edades en lote

# PROCESO
# clasificar con if/elif, agrupar en diccionario

# SALIDA
# diccionario agrupado, promedio

# EJEMPLO DE ENTRADA
# ae = AgrupadorEdades()
# ae.agrupar_por_categoria(5, 15, 30, 70)

# SALIDA ESPERADA
# {'niño': [5], 'adolescente': [15], 'adulto': [30], 'mayor': [70]}

# Colecciones: diccionario de listas (estructura anidada)


class AgrupadorEdades:

    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in self.grupos:
                self.grupos[categoria] = []
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.grupos or not self.grupos[categoria]:
            return 0.0
        edades_cat = self.grupos[categoria]
        return sum(edades_cat) / len(edades_cat)


# DEPURACIÓN / PRUEBA DE ESCRITORIO
# ae = AgrupadorEdades()

# 1. Probar clasificar_edad:
# ae.clasificar_edad(5)  -> 5 < 12  -> Retorna "niño"
# ae.clasificar_edad(15) -> 15 < 18 -> Retorna "adolescente"
# ae.clasificar_edad(30) -> 30 < 60 -> Retorna "adulto"
# ae.clasificar_edad(70) -> 70 >= 60 -> Retorna "mayor"

# 2. Probar agrupar_por_categoria:
# ae.agrupar_por_categoria(5, 15, 30, 70)
# -> edad = 5:  cat = "niño"        -> self.grupos['niño'] = [5]
# -> edad = 15: cat = "adolescente" -> self.grupos['adolescente'] = [15]
# -> edad = 30: cat = "adulto"      -> self.grupos['adulto'] = [30]
# -> edad = 70: cat = "mayor"       -> self.grupos['mayor'] = [70]
# -> Retorna: {'niño': [5], 'adolescente': [15], 'adulto': [30], 'mayor': [70]}

# 3. Probar edad_promedio_categoria:
# ae.edad_promedio_categoria("adulto") -> sum([30]) / len([30]) -> 30.0 / 1 -> Retorna 30.0