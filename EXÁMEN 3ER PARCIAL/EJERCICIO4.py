print("Martínez Estrada Ricardo / NO. de control: 1193 / 29.11.2024 / Exámen 3ra Unidad")
print(" ")

# Definimos la clase Calculadora
class Calculadora:
    def __init__(self, num1, num2):
        # El constructor recibe dos números enteros
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        # Método para sumar los dos números
        return self.num1 + self.num2

    def resta(self):
        # Método para restar los dos números
        return self.num1 - self.num2

    def multiplicacion(self):
        # Método para multiplicar los dos números
        return self.num1 * self.num2

    def division(self):
        # Método para dividir los dos números, manejando la división por cero
        if self.num2 == 0:
            return "Error: División por cero"
        else:
            return self.num1 / self.num2

# Función principal que ejecuta el programa
def ejecutar_calculadora():
    # Pedimos al usuario que ingrese dos números enteros
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    
    # Creamos una instancia de la clase Calculadora
    calc = Calculadora(num1, num2)
    
    # Realizamos las operaciones y mostramos los resultados
    print(f"Suma: {calc.suma()}")
    print(f"Resta: {calc.resta()}")
    print(f"Multiplicación: {calc.multiplicacion()}")
    print(f"División: {calc.division()}")

# Ejecutamos la calculadora
if __name__ == "__main__":
    ejecutar_calculadora()