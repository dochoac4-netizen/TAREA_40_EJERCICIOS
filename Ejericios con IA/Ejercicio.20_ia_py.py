# Ej. 20 AVANZADO  Analizador de patrones en textos

# Clase AnalizadorPatrones que:
# (1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista;
# (2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]};
# (3) tenga método palabras_unicas(texto) usando un conjunto.

# ENTRADA
# texto y patrón de búsqueda

# PROCESO
# split(), filtrar, agrupar por longitud, eliminar duplicados

# SALIDA
# listas, diccionario, conjunto

# EJEMPLO DE ENTRADA
# ap = AnalizadorPatrones()
# ap.agrupar_por_longitud("el gato está aquí")

# SALIDA ESPERADA (Formato correcto de Python)
# {2: ['el'], 4: ['gato', 'está', 'aquí']}

# Colecciones: todas (lista, diccionario, conjunto) + métodos de string (split, startswith)


class AnalizadorPatrones:

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []
        for p in palabras:
            if p.startswith(patron):
                resultado.append(p)
        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        grupos = {}
        for p in palabras:
            l = len(p)
            if l not in grupos:
                grupos[l] = []
            grupos[l].append(p)
        return grupos

    def palabras_unicas(self, texto):
        palabras = texto.split()
        return set(palabras)


# DEPURACIÓN / PRUEBA DE ESCRITORIO
# ap = AnalizadorPatrones()

# 1. probar encontrar_palabras:
# ap.encontrar_palabras("el gato está aquí", "es") -> Retorna ['está']

# 2. probar agrupar_por_longitud:
# ap.agrupar_por_longitud("el gato está aquí")
# -> 'el'   (len 2): grupos[2] = ['el']
# -> 'gato' (len 4): grupos[4] = ['gato']
# -> 'está' (len 4): grupos[4].append('está') -> ['gato', 'está']
# -> 'aquí' (len 4): grupos[4].append('aquí') -> ['gato', 'está', 'aquí']
# -> Retorna: {2: ['el'], 4: ['gato', 'está', 'aquí']}

# 3. probar palabras_unicas:
# ap.palabras_unicas("el gato está aquí") -> Retorna {'el', 'gato', 'está' 'aquí'}