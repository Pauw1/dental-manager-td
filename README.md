# Gestor de Tratamientos Dentales - DentalManager 🦷

Este proyecto es la **Evaluación de Portafolio** para el Módulo 3 de Python. Es una aplicación de línea de comandos (CLI) diseñada para simular la gestión de pacientes y tratamientos en una clínica dental.

El objetivo principal es demostrar el dominio de los conceptos fundamentales de Python en un solo proyecto cohesivo.

## Descripción del Proyecto

`DentalManager` es un sistema simple que se ejecuta en la terminal y utiliza una lista de diccionarios en memoria para funcionar como una base de datos temporal. Permite al administrador de la clínica realizar operaciones CRUD (Crear, Leer, Actualizar) sobre los registros de los pacientes.

## Características Implementadas

Este proyecto pone en práctica todos los requisitos de la evaluación:

* **Variables y Tipos de Datos:** Se utilizan `string`, `int`, `float` y `bool` para capturar y almacenar la información del paciente (nombre, edad, saldo, estado activo).
* **Estructuras de Datos:**
    * **Lista:** Se usa una lista principal (`pacientes_db`) para almacenar a todos los pacientes.
    * **Diccionarios:** Cada paciente es un diccionario.
    * **Estructuras Anidadas:** Cada paciente (diccionario) contiene una lista de tratamientos (otra lista de diccionarios).
* **Sentencias Condicionales:** Se usa `if`, `elif`, y `else` para controlar el flujo de los menús, validar entradas (ej. pagos) y tomar decisiones.
* **Sentencias Iterativas:**
    * **`while True`**: Se usa para el bucle principal del menú y el submenú de gestión.
    * **`for`**: Se usa para iterar la base de datos (`buscar_paciente`, `mostrar_todos_pacientes`) y para iterar los tratamientos de un paciente (`ver_ficha_paciente`).
* **Modularización con Funciones:** Todo el código está encapsulado en funciones con responsabilidades únicas (ej. `agregar_paciente`, `registrar_pago`, `mostrar_menu`).
* **Gestión de Código Fuente:** El proyecto se mantiene en este repositorio de GitHub con un historial de 3 commits que reflejan el progreso incremental.

## Cómo Ejecutar el Programa

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Clona este repositorio en tu máquina local.
3.  Abre una terminal y navega hasta la carpeta del proyecto.
4.  Ejecuta el script principal:

    ```bash
    python dental_manager.py
    ```

5.  Sigue las instrucciones que aparecen en el menú de la consola.
