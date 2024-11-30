print("Martínez Estrada Ricardo / NO. de control: 1193 / 29.11.2024 / Exámen 3ra Unidad")
print(" ")

# Definimos la clase Triangulo
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        # Inicializamos los lados del triángulo
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        # Devuelve el valor del lado más grande del triángulo
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        # Determina el tipo de triángulo según los lados
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"  # Todos los lados son iguales
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"  # Dos lados son iguales
        else:
            return "Escaleno"  # Ningún lado es igual

# Función principal para interactuar con el usuario
def cargar_triangulo():
    # Pedimos los tres lados del triángulo
    lado1 = float(input("Introduce el primer lado del triángulo: "))
    lado2 = float(input("Introduce el segundo lado del triángulo: "))
    lado3 = float(input("Introduce el tercer lado del triángulo: "))
    
    # Creamos una instancia de la clase Triangulo
    triangulo = Triangulo(lado1, lado2, lado3)
    
    # Mostramos el valor del lado más grande y el tipo de triángulo
    print(f"El lado más grande es: {triangulo.lado_mayor()}")
    print(f"El tipo de triángulo es: {triangulo.tipo_triangulo()}")

# Ejecutamos el programa
if __name__ == "__main__":
    cargar_triangulo()