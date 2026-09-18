# EJERCICIO 2 - Contador de palabras únicas

# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# palabras individuales o en lotes (*args)
# PROCESO:
# guardar palabras en un conjunto (para evitar duplicados) y en una lista (para preservar el orden), contar únicas
# SALIDA:
# cantidad de palabras únicas (entero)
# Ejemplo de entrada:
# at = AnalizadorTexto()
# at.agregar_multiples("hola", "mundo", "hola")
# at.contar_palabras()
# Salida esperada:
# 2


# 2. BOSQUEJO
# Instancia: at = AnalizadorTexto() -> self.conjunto = set(), self.lista = []
#
# Método agregar_palabra(palabra):
#   - Insertar palabra en el conjunto con .add()
#   - Insertar palabra en la lista con .append()
#
# Método agregar_multiples("hola", "mundo", "hola"):
#   - Recorrer cada elemento en *args y reutilizar self.agregar_palabra(p)
#
# Método contar_palabras():
#   - Devolver la cantidad de elementos en el conjunto usando len(self.conjunto)
#   - len({"hola", "mundo"}) = 2


# 3. PATRON
# Uso coordinado de dos colecciones: un Conjunto (`set`) para unicidad y una Lista (`list`) para mantener orden de inserción.
# Reutilización de métodos de instancia llamando a `self.agregar_palabra()` desde `agregar_multiples()`.


# 4. CODIGO
class AnalizadorTexto:

    def __init__(self):
        self.palabras_unicas = set()
        self.historial_ordenado = []

    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)
        self.historial_ordenado.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


# 5. PRUEBA / DEPURACION
# Instanciación:
# at = AnalizadorTexto()
# self.palabras_unicas = set()
# self.historial_ordenado = []
#
# Ejecución 1: at.agregar_multiples("hola", "mundo", "hola")
# - "hola"  -> set.add("hola")  -> {'hola'},  list.append("hola")  -> ["hola"]
# - "mundo" -> set.add("mundo") -> {'hola', 'mundo'}, list.append("mundo") -> ["hola", "mundo"]
# - "hola"  -> set.add("hola")  -> {'hola', 'mundo'}, list.append("hola")  -> ["hola", "mundo", "hola"]
#
# Ejecución 2: at.contar_palabras()
# - len({'hola', 'mundo'}) = 2
# Retorna: 2