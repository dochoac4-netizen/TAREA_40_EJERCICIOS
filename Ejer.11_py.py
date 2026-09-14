class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


# --- Ejemplo de uso ---
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())