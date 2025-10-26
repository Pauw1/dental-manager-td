# Proyecto de Portafolio - Gestor de Tratamientos Dentales

def mostrar_menu():

    print("\n 🦷 DentalManager")
    print("1. Agregar nuevo paciente")
    print("2. Buscar paciente y gestionar")
    print("3. Mostrar todos los pacientes")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion_principal = input("Seleccione una opción (1-4): ").strip()

        if opcion_principal == '1':
            print("1. Agregar nuevo paciente")
            
        elif opcion_principal == '2':
            print("2. Buscar paciente y gestionar")
                
        elif opcion_principal == '3':
            print("3. Mostrar todos los pacientes")
            
        elif opcion_principal == '4':
            print("\nHas salido de DentalManager")
            break 
            
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()