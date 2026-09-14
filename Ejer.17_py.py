class AgrupadorEdades:

    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        for cat in self.grupos:
            self.grupos[cat] = []
        for edad in edades:
            cat = self.clasificar_edad(edad)
            self.grupos[cat].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])
        if not edades:
            return 0.0
        return sum(edades) / len(edades)


# --- Ejemplo de uso ---
ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))