class AnalizadorTexto:

    def __init__(self):
        self.conjunto_palabras = set()
        self.lista_palabras = []

    def agregar_palabra(self, palabra):
        if palabra not in self.conjunto_palabras:
            self.lista_palabras.append(palabra)
        self.conjunto_palabras.add(palabra)

    def contar_palabras(self):
        return len(self.conjunto_palabras)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


# --- Ejemplo de uso ---
at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())