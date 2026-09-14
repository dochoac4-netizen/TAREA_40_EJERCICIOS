class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = "".join(
            self.codificar_letra(c, desplazamiento) for c in palabra
        )
        self.historial[palabra] = resultado
        return resultado


# --- Ejemplo de uso ---
cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))