class AnalizadorPatrones:

    def __init__(self):
        self.palabras_analizadas = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        self.palabras_analizadas.update(palabras)
        return [p for p in palabras if p.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        self.palabras_analizadas.update(palabras)
        agrupadas = {}
        for p in palabras:
            longitud = len(p)
            if longitud not in agrupadas:
                agrupadas[longitud] = []
            agrupadas[longitud].append(p)
        return agrupadas

    def palabras_unicas(self):
        return self.palabras_analizadas


# --- Ejemplo de uso ---
ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato está aquí"))