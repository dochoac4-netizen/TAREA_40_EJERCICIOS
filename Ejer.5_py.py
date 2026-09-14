class AnalizadorNumeros:

    def __init__(self):
        self.ultimos_pares = []
        self.ultimos_impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.ultimos_pares = []
        self.ultimos_impares = []

        for num in numeros:
            if self.es_par(num):
                self.ultimos_pares.append(num)
            else:
                self.ultimos_impares.append(num)

        return {"pares": self.ultimos_pares, "impares": self.ultimos_impares}

    def cantidad_pares_impares(self):
        return (len(self.ultimos_pares), len(self.ultimos_impares))


# --- Ejemplo de uso ---
an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())