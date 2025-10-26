
pacientes_db = []

def mostrar_menu():
    print("\n🦷 DentalManager")
    print("1. Agregar nuevo paciente")
    print("2. Buscar paciente y gestionar")
    print("3. Mostrar todos los pacientes")
    print("4. Salir")

def mostrar_submenu_paciente(nombre_paciente):

    print(f"\nGestionando a: {nombre_paciente}")
    print("1. Ver ficha completa del paciente")
    print("2. Agregar tratamiento")
    print("3. Registrar pago")
    print("4. Volver al menú principal")

def buscar_paciente(rut):
    """
    Busca un paciente en la 'base de datos' (la lista) por su RUT.
    Devuelve el diccionario del paciente si lo encuentra, o None si no.
    """
    for paciente in pacientes_db:
        if paciente["rut"] == rut:
            return paciente
    return None

def agregar_paciente():
    """
    Pide datos al usuario y crea un nuevo paciente (diccionario).
    """
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
        print(f"RUT: {paciente['rut']} | Nombre: {paciente['nombre']} | Saldo: ${paciente['saldo_pendiente']:,.0f} | Estado: {estado}")

def ver_ficha_paciente(paciente):

    print(f"\n--- Ficha del Paciente: {paciente['nombre']} ---")
    print(f"RUT:           {paciente['rut']}")
    print(f"Edad:          {paciente['edad']} años")
    print(f"Teléfono:      {paciente['telefono']}")
    
    estado = "Activo" if paciente["activo"] else "Inactivo (Sin previsión)"
    print(f"Estado:        {estado}")
    
    print(f"Saldo Pendiente: ${paciente['saldo_pendiente']:,.0f}")

    print("\nTratamientos")

    if not paciente["tratamientos"]:
        print("No hay tratamientos registrados para este paciente.")
    else:
        for i, tratamiento in enumerate(paciente["tratamientos"], 1):
            print(f"  {i}. {tratamiento['descripcion']}")
            print(f"     Costo: ${tratamiento['costo']:,.0f} - Estado: {tratamiento['estado']}")

def agregar_tratamiento(paciente):
    print("\n Agregar Tratamiento")
    
    descripcion = input("Descripción del tratamiento (ej. Limpieza Dental): ").strip()
    
    try:
        costo = float(input("Costo del tratamiento (ej. 50000): "))
    except ValueError:
        print("Error: El costo debe ser un valor numérico.")
        return
    
    if costo < 0:
        print("Error: El costo no puede ser negativo.")
        return

    nuevo_tratamiento = {
        "descripcion": descripcion,
        "costo": costo,
        "estado": "Pendiente de pago"
    }
    
    paciente["tratamientos"].append(nuevo_tratamiento)
    
    paciente["saldo_pendiente"] += costo
    
    print(f"Tratamiento '{descripcion}' agregado con éxito.")
    print(f"Nuevo saldo pendiente: ${paciente['saldo_pendiente']:,.0f}")

def registrar_pago(paciente):
    print("\nRegistrar Pago")
    saldo_actual = paciente["saldo_pendiente"]
    
    if saldo_actual <= 0:
        print(f"El paciente {paciente['nombre']} no tiene saldo pendiente.")
        return

    print(f"El saldo pendiente actual es: ${saldo_actual:,.0f}")
    
    try:
        monto_pago = float(input("Ingrese el monto a pagar: "))
    except ValueError:
        print("Error: El monto debe ser un valor numérico.")
        return

    if monto_pago <= 0:
        print("Error: El monto del pago debe ser positivo.")
    elif monto_pago > saldo_actual:
        print(f"Error: El pago (${monto_pago:,.0f}) excede el saldo pendiente (${saldo_actual:,.0f}).")
    else:
        paciente["saldo_pendiente"] -= monto_pago
        print("¡Pago registrado con éxito!")
        print(f"Saldo restante: ${paciente['saldo_pendiente']:,.0f}")
        
        if paciente["saldo_pendiente"] == 0:
            for t in paciente["tratamientos"]:
                t["estado"] = "Pagado"
            print("Todos los tratamientos han sido marcados como 'Pagado'.")

def gestionar_paciente(paciente):
    while True:
        mostrar_submenu_paciente(paciente["nombre"])
        sub_opcion = input("Seleccione una opción (1-4): ").strip()

        if sub_opcion == '1':
            ver_ficha_paciente(paciente)
        
        elif sub_opcion == '2':
            agregar_tratamiento(paciente)
            
        elif sub_opcion == '3':
            registrar_pago(paciente)
            
        elif sub_opcion == '4':
            print(f"Volviendo al menú principal...")
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")


def main():
    while True:
        mostrar_menu()
        opcion_principal = input("Seleccione una opción (1-4): ").strip()
        
        if opcion_principal == '1':
            agregar_paciente()
            
        elif opcion_principal == '2':
            print("\n2. Buscar Paciente y Gestionar")
            rut_buscar = input("Ingrese el RUT del paciente a gestionar: ").strip()
            paciente_encontrado = buscar_paciente(rut_buscar)
            
            if paciente_encontrado:
        
                gestionar_paciente(paciente_encontrado)
            else:
                print(f"Error: No se encontró ningún paciente con el RUT {rut_buscar}.")
                
        elif opcion_principal == '3':
            mostrar_todos_pacientes()
            
        elif opcion_principal == '4':
            print("\nSaliendo de DentalManager")
            break
            
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()