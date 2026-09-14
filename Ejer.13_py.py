class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []
        max_len = max(len(lista1), len(lista2))
        for i in range(max_len):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []
        resultado = listas[0]
        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)
        return resultado


# --- Ejemplo de uso ---
cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))