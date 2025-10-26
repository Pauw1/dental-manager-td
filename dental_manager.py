# Dental Manager

pacientes_db = []

def mostrar_menu():
    print("\n🦷 DentalManager")
    print("1. Agregar nuevo paciente")
    print("2. Buscar paciente")
    print("3. Mostrar todos los pacientes")
    print("4. Salir")

def buscar_paciente(rut):

    for paciente in pacientes_db:
        if paciente["rut"] == rut:
            return paciente
    return None

def agregar_paciente():

    print("\n1. Agregar Nuevo Paciente")
    
    rut = input("Ingrese RUT (ej. 12345678-9): ").strip()

    if buscar_paciente(rut) is not None:
        print(f"Error: El RUT {rut} ya está registrado.")
        return

    nombre = input("Ingrese nombre completo: ").strip()
    
    try:
        edad = int(input("Ingrese edad: "))
    except ValueError:
        print("Error: La edad debe ser un número.")
        return
        
    telefono = input("Ingrese teléfono (ej. +569...): ").strip()
    
    tiene_prevision_input = input("¿Tiene previsión de salud? (s/n): ").lower().strip()
    es_paciente_activo = (tiene_prevision_input == 's')

    nuevo_paciente = {
        "rut": rut,
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono,
        "activo": es_paciente_activo,
        "saldo_pendiente": 0.0,
        "tratamientos": []
    }

    pacientes_db.append(nuevo_paciente)
    print(f"¡Paciente {nombre} (RUT: {rut}) agregado con éxito!")

def mostrar_todos_pacientes():

    print("\n3. Lista de Todos los Pacientes")
    
    if not pacientes_db:
        print("No hay pacientes registrados en el sistema.")
        return

    print(f"Total de pacientes: {len(pacientes_db)}")

    for paciente in pacientes_db:
        estado = "Activo" if paciente["activo"] else "Inactivo"
        print(f"RUT: {paciente['rut']} | Nombre: {paciente['nombre']} | Estado: {estado}")

def main():

    while True:
        mostrar_menu()
        opcion_principal = input("Seleccione una opción (1-4): ").strip()


        if opcion_principal == '1':
            agregar_paciente()
            
        elif opcion_principal == '2':
            print("\n--- 2. Buscar Paciente ---")
            rut_buscar = input("Ingrese el RUT del paciente a buscar: ").strip()
            paciente_encontrado = buscar_paciente(rut_buscar)
            
            if paciente_encontrado:
                print(f"¡Paciente encontrado!")
                print(f"Nombre: {paciente_encontrado['nombre']}")
                print(f"Teléfono: {paciente_encontrado['telefono']}")

            else:
                print(f"Error: No se encontró ningún paciente con el RUT {rut_buscar}.")
                
        elif opcion_principal == '3':
            mostrar_todos_pacientes()
            
        elif opcion_principal == '4':
            print("\nSaliendo de DentalManager... ¡Adiós! 👋")
            break
            
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()