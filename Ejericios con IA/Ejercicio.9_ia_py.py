# EJERCICIO DE PRÁCTICA - CLASIFICADOR DE CARACTERES EN TEXTO

# 1. ENTENDER EL PROBLEMA
# ENTRADA: textos para analizar
# PROCESO: recorrer carácter a carácter, clasificar
# SALIDA: diccionario con conteos
# EJEMPLO DE ENTRADA:
# ac = AnalizadorCadena()
# ac.contar_por_tipo("Py45!")
# SALIDA ESPERADA:
# {'letras': 2, 'digitos': 2, 'especiales': 1}


# 2. BOSQUEJO
# Analizar "Py45!":
#   'P' -> letra    -> letras = 1
#   'y' -> letra    -> letras = 2
#   '4' -> digito   -> digitos = 1
#   '5' -> digito   -> digitos = 2
#   '!' -> especial -> especiales = 1
#
# Texto más largo:
#   len("Py45!") = 5 -> self.texto_mas_largo = "Py45!"


# 3. PATRON
# Colecciones: diccionario para contar tipos


# 4. CODIGO
class AnalizadorCadena:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_letras(self, caracter):
        return caracter.isalpha()

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteos = {'letras': 0, 'digitos': 0, 'especiales': 0}

        for char in texto:
            if self.solo_letras(char):
                conteos['letras'] += 1
            elif char.isdigit():
                conteos['digitos'] += 1
            else:
                conteos['especiales'] += 1

        return conteos


# 5. PRUEBA / DEPURACION
# ac = AnalizadorCadena() -> self.texto_mas_largo = ""

# contar_por_tipo("Py45!")
# len("Py45!") = 5 > 0 -> self.texto_mas_largo = "Py45!"
# char = 'P' -> es_letra = True  -> 'letras': 1
# char = 'y' -> es_letra = True  -> 'letras': 2
# char = '4' -> es_digito = True -> 'digitos': 1
# char = '5' -> es_digito = True -> 'digitos': 2
# char = '!' -> especial        -> 'especiales': 1
# Retorna: {'letras': 2, 'digitos': 2, 'especiales': 1}