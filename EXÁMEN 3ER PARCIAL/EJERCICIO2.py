print("Martínez Estrada Ricardo / NO. de control: 1193 / 29.11.2024 / Exámen 3ra Unidad")
print(" ")

# Definimos la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        # Inicializamos los atributos de la persona
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        # Muestra el nombre y la edad de la persona
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def es_mayor_de_edad(self):
        # Verifica si la persona es mayor de edad (18 años o más)
        if self.edad >= 18:
            return True
        else:
            return False

# Función principal para interactuar con el usuario
def cargar_persona():
    # Pedimos el nombre y la edad de la persona
    nombre = input("Introduce el nombre de la persona: ")
    edad = int(input("Introduce la edad de la persona: "))
    
    # Creamos una instancia de la clase Persona
    persona = Persona(nombre, edad)
    
    # Mostramos los datos de la persona
    persona.mostrar_datos()
    
    # Verificamos si la persona es mayor de edad
    if persona.es_mayor_de_edad():
        print(f"{persona.nombre} es mayor de edad.")
    else:
        print(f"{persona.nombre} es menor de edad.")

# Ejecutamos el programa
if __name__ == "__main__":
    cargar_persona()