# EJERCICIO 16 - Codificador/Decodificador (Cifrado César)

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# letra/palabra y desplazamiento (1-25)
# PROCESO:
# convertir a código ASCII, desplazar con %, guardar historial
# SALIDA:
# palabra codificada
# Ejemplo de entrada:
# cc = CodificadorCesar()
# cc.codificar_palabra("hola", 3)
# Salida esperada:
# "kroc" (aproximadamente, según desplazamiento)

# 2. BOSQUEJO
# Instancia: cc = CodificadorCesar() -> self.historial = {}
#
# Método codificar_letra('a', 3):
#   - Convertir 'a' a su posición (0-25) respecto a 'a': ord('a') - ord('a') = 0
#   - Sumar desplazamiento y aplicar módulo 26: (0 + 3) % 26 = 3
#   - Volver a carácter ASCII: chr(ord('a') + 3) -> 'd'
#
# Método codificar_palabra("hola", 3):
#   - Iterar cada letra:
#       'h' -> 'k'
#       'o' -> 'r'
#       'l' -> 'o'
#       'a' -> 'd'
#   - Unir caracteres en string: "krod"
#   - Guardar en diccionario de historial: self.historial["hola"] = "krod"
#   - Retornar "krod"

# 3. PATRON
# Uso de funciones built-in `ord()` para obtener el valor numérico ASCII y `chr()` para retornar a carácter.
# Uso de aritmética modular `(posicion + desplazamiento) % 26` para reiniciar el ciclo en el abecedario.
# Registro del resultado en un atributo interno tipo diccionario como historial de operaciones.


# 4. CODIGO
class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if "a" <= letra <= "z":
            base = ord("a")
            nueva_pos = (ord(letra) - base + desplazamiento) % 26
            return chr(base + nueva_pos)
        elif "A" <= letra <= "Z":
            base = ord("A")
            nueva_pos = (ord(letra) - base + desplazamiento) % 26
            return chr(base + nueva_pos)
        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = ""
        for letra in palabra:
            codificada += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = codificada
        return codificada


# 5. PRUEBA / DEPURACION
# Instanciación:
# cc = CodificadorCesar() -> self.historial = {}
#
# Ejecución: cc.codificar_palabra("hola", 3)
# Paso 1: 'h' -> ord('h') - ord('a') = 104 - 97 = 7
#   - (7 + 3) % 26 = 10 -> chr(97 + 10) = 'k'
# Paso 2: 'o' -> ord('o') - ord('a') = 111 - 97 = 14
#   - (14 + 3) % 26 = 17 -> chr(97 + 17) = 'r'
# Paso 3: 'l' -> ord('l') - ord('a') = 108 - 97 = 11
#   - (11 + 3) % 26 = 14 -> chr(97 + 14) = 'o'
# Paso 4: 'a' -> ord('a') - ord('a') = 97 - 97 = 0
#   - (0 + 3) % 26 = 3 -> chr(97 + 3) = 'd'
#
# Resultado acumulado: "krod"
# Guardado en historial: self.historial["hola"] = "krod"
# Resultado final: "krod"