class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = [i for i in range(1, numero + 1) if numero % i == 0]
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        divisores_propios = divisores[:-1]
        return sum(divisores_propios) == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for num in numeros:
            resultado[num] = self.encontrar_divisores(num)
        return resultado


# --- Ejemplo de uso ---
df = DivisorFinder()
print(df.encontrar_divisores(12))