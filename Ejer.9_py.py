# EJERCICIO 9 - Validador de caracteres

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# textos para analizar
# PROCESO:
# recorrer carácter a carácter, clasificar
# SALIDA:
# diccionario con conteos
# Ejemplo de entrada:
# astr = AnalizadorString()
# astr.contar_por_tipo("Hola123")
# Salida esperada:
# {'vocales': 2, 'consonantes': 2, 'digitos': 3}


# 2. BOSQUEJO
# Instancia: astr = AnalizadorString() -> self.texto_mas_largo = ""
#
# Método solo_vocales(letra):
#   - Verificar si letra.lower() está en "aeiou"
#
# Método contar_por_tipo("Hola123"):
#   - Actualizar self.texto_mas_largo si len("Hola123") > len(self.texto_mas_largo)
#   - Recorrer cada carácter de "Hola123":
#       * Si es dígito (caracter.isdigit()): sumar a digitos
#       * Si es letra (caracter.isalpha()):
#           - Si solo_vocales(caracter): sumar a vocales
#           - Si no: sumar a consonantes
#   - Retornar {'vocales': 2, 'consonantes': 2, 'digitos': 3}


# 3. PATRON
# Métodos de cadenas de Python: `.isalpha()`, `.isdigit()`, `.lower()`.
# Reutilización del método `solo_vocales()` dentro de `contar_por_tipo()`.
# Atributo de instancia para guardar un estado global persistente (`self.texto_mas_largo`).


# 4. CODIGO
class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteos = {"vocales": 0, "consonantes": 0, "digitos": 0}

        for caracter in texto:
            if caracter.isdigit():
                conteos["digitos"] += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    conteos["vocales"] += 1
                else:
                    conteos["consonantes"] += 1

        return conteos


# 5. PRUEBA / DEPURACION
# Instanciación:
# astr = AnalizadorString() -> self.texto_mas_largo = ""
#
# Ejecución: astr.contar_por_tipo("Hola123")
# - len("Hola123") (7) > len("") (0) -> self.texto_mas_largo = "Hola123"
# - 'H': es alpha, no es vocal -> consonantes: 1
# - 'o': es alpha, es vocal     -> vocales: 1
# - 'l': es alpha, no es vocal -> consonantes: 2
# - 'a': es alpha, es vocal     -> vocales: 2
# - '1': es dígito             -> digitos: 1
# - '2': es dígito             -> digitos: 2
# - '3': es dígito             -> digitos: 3
# Retorna: {'vocales': 2, 'consonantes': 2, 'digitos': 3}