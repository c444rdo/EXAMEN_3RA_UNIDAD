print("Martínez Estrada Ricardo / NO. de control: 1193 / 29.11.2024 / Exámen 3ra Unidad")
print(" ")

# Clase que representa un Contacto con nombre, teléfono y email
class Contacto:
    def __init__(self, nombre, telefono, email):
        # Inicializamos los atributos del contacto
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        # Representación en formato de texto del contacto
        return f"{self.nombre} - {self.telefono} - {self.email}"

# Clase que gestiona la Agenda de contactos
class Agenda:
    def __init__(self):
        # Lista donde se almacenarán los contactos
        self.contactos = []

    def agregar_contacto(self):
        # Solicita al usuario los datos de un nuevo contacto y lo añade a la lista
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        # Creamos un nuevo objeto Contacto y lo añadimos a la lista de contactos
        self.contactos.append(Contacto(nombre, telefono, email))

    def listar_contactos(self):
        # Muestra todos los contactos de la lista
        for contacto in self.contactos:
            print(contacto)

    def buscar_contacto(self):
        # Solicita el nombre de un contacto para buscarlo
        nombre = input("Buscar por nombre: ")
        # Recorre la lista de contactos y busca un contacto por su nombre
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():  # Comparación sin importar mayúsculas/minúsculas
                print(contacto)  # Si lo encuentra, lo muestra
                return
        print("No encontrado.")  # Si no encuentra el contacto, muestra un mensaje

    def editar_contacto(self):
        # Solicita el nombre de un contacto para editarlo
        nombre = input("Editar nombre: ")
        # Recorre la lista de contactos buscando por nombre
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                # Si lo encuentra, permite modificar los datos
                contacto.nombre = input("Nuevo nombre: ")
                contacto.telefono = input("Nuevo teléfono: ")
                contacto.email = input("Nuevo email: ")
                print("Contacto actualizado.")  # Confirma la actualización
                return
        print("No encontrado.")  # Si no encuentra el contacto, muestra un mensaje

# Función que muestra el menú con las opciones disponibles
def mostrar_menu():
    # Muestra las opciones del menú para que el usuario elija
    print("\n1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Salir")
    return input("Elige una opción: ")  # Lee la opción seleccionada

# Función principal que ejecuta la agenda
def ejecutar_agenda():
    agenda = Agenda()  # Creamos una instancia de la clase Agenda
    while True:
        opcion = mostrar_menu()  # Mostramos el menú y obtenemos la opción del usuario
        if opcion == '1':
            agenda.agregar_contacto()  # Si se elige 1, se añade un nuevo contacto
        elif opcion == '2':
            agenda.listar_contactos()  # Si se elige 2, se listan todos los contactos
        elif opcion == '3':
            agenda.buscar_contacto()  # Si se elige 3, se busca un contacto por nombre
        elif opcion == '4':
            agenda.editar_contacto()  # Si se elige 4, se edita un contacto
        elif opcion == '5':
            print("Adiós!")  # Si se elige 5, se cierra el programa
            break
        else:
            print("Opción no válida.")  # Si la opción no es válida, se muestra un mensaje

# Si el archivo se ejecuta directamente, se llama a la función ejecutar_agenda
if __name__ == "__main__":
    ejecutar_agenda()