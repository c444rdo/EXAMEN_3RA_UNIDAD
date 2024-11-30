print("Martínez Estrada Ricardo / NO. de control: 1193 / 29.11.2024 / Exámen 3ra Unidad")
print(" ")

# Definimos la clase Alumno
class Alumno:
    def __init__(self, nombre, nota):
        # Inicializamos los atributos de la clase Alumno
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        # Muestra el nombre y la nota del alumno
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        # Muestra un mensaje si el alumno ha aprobado o no (aprobado si la nota es >= 5)
        if self.nota >= 5:
            return f"{self.nombre} ha aprobado."
        else:
            return f"{self.nombre} ha suspendido."

# Función principal para interactuar con el usuario
def cargar_alumno():
    # Pedimos el nombre y la nota del alumno
    nombre = input("Introduce el nombre del alumno: ")
    nota = float(input("Introduce la nota del alumno: "))
    
    # Creamos una instancia de la clase Alumno
    alumno = Alumno(nombre, nota)
    
    # Mostramos los datos del alumno
    alumno.mostrar_datos()
    
    # Mostramos el resultado del alumno (aprobado o suspendido)
    print(alumno.resultado())

# Ejecutamos el programa
if __name__ == "__main__":
    cargar_alumno()