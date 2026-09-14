class SelectorRango:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos_unicos = set()
        for inicio, fin in rangos:
            elementos_unicos.update(self.crear_rango(inicio, fin))
        return sorted(list(elementos_unicos))


# --- Ejemplo de uso ---
sr = SelectorRango()
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))