# Modulo empleados.py

# Importaciones
import os
import re

# Importacion del modulo utils.py
from utils import leer_empleados, generar_lista_empleados_txt, generar_empleado_info_txt, validar_correo, RESET_COLOR, GREEN, RED, CYAN, MAGENTA

# FUNCION 1: Nuevos Empleados
def ingresar_empleado():

    """
    Función para ingresar un nuevo empleado y guardar su información en un archivo de texto.
    Solicita los datos del empleado y los valida antes de almacenarlos.
    """
    
# Mensaje Inicial   
    print(f"{MAGENTA}-----------------------------------------------------------")
    print("Ingrese los datos del nuevo empleado:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")


# Leer la lista actual de empleados
    empleados = leer_empleados()

   
# Solicitar y validar el ID del empleado
    while True:
        id_empleado = input(f"{CYAN}‣ ID del empleado: {RESET_COLOR}").strip()
        if not id_empleado:
            print(f"{RED}El ID del empleado no puede estar vacío.{RESET_COLOR}")
            continue
        if any(emp['ID del empleado'] == id_empleado for emp in empleados):
            print(f"{RED}-----------------------------------------------------------")
            print(f"El empleado ya existe en la planilla.{RESET_COLOR}")
            return
        break


# Solicitar el nombre del empleado 
    while True:
        nombre = input(f"{CYAN}‣ Nombre del empleado: {RESET_COLOR}").strip().lower()
        if not nombre:
            print(f"{RED}El nombre del empleado no puede estar vacío.{RESET_COLOR}")
            continue
        break


# Solicitar el puesto de trabajo del empleado
    while True:
        puesto = input(f"{CYAN}‣ Puesto de trabajo: {RESET_COLOR}").strip().lower()
        if not puesto:
            print(f"{RED}El puesto de trabajo no puede estar vacío.{RESET_COLOR}")
            continue
        break

   
# Solicitar y validar el sexo del empleado
    while True:
        sexo = input(f"{CYAN}‣ Sexo (m/f): {RESET_COLOR}").strip().lower()
        if sexo not in ['m', 'f']:
            print(f"{RED}El sexo debe ser 'm' para masculino o 'f' para femenino.{RESET_COLOR}")
            continue
        break

 
# Solicitar y validar la edad del empleado
    while True:
        try:
            edad = int(input(f"{CYAN}‣ Edad: {RESET_COLOR}").strip())
            if edad <= 0:
                print(f"{RED}La edad debe ser un número positivo.{RESET_COLOR}")
                continue
            break
        except ValueError:
            print(f"{RED}Por favor, ingrese un número válido para la edad.{RESET_COLOR}")


# Solicitar y validar el teléfono del empleado
    while True:
        telefono = input(f"{CYAN}‣ Teléfono: {RESET_COLOR}").strip()
        if not re.match(r'^\+?[0-9\s\-\(\)]+$', telefono):
            print(f"{RED}El teléfono solo puede contener números, espacios, y los caracteres +, -, (, ).{RESET_COLOR}")
            continue
        break


# Solicitar y validar el correo electrónico del empleado
    while True:
        correo = input(f"{CYAN}‣ Correo electrónico: {RESET_COLOR}").strip()
        if not validar_correo(correo):
            print(f"{RED}El formato del correo electrónico no es válido.{RESET_COLOR}")
            continue
        break    


# Solicitar y validar el salario base del empleado
    while True:
        try:
            salario_base = float(input(f"{CYAN}‣ Salario Base: {RESET_COLOR}").strip())
            if salario_base <= 0:
                print(f"{RED}El salario base debe ser un número positivo.{RESET_COLOR}")
                continue
            break
        except ValueError:
            print(f"{RED}Por favor, ingrese un número válido para el salario base.{RESET_COLOR}")


# Mostrar los datos ingresados
    print(f"{MAGENTA}-----------------------------------------------------------")
    print(f"Por favor, confirme los datos ingresados:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    print(f"ID del empleado: {id_empleado}")
    print(f"Nombre: {nombre}")
    print(f"Puesto de trabajo: {puesto}")
    print(f"Sexo: {sexo}")
    print(f"Edad: {edad}")
    print(f"Teléfono: {telefono}")
    print(f"Correo electrónico: {correo}")
    print(f"Salario Base: {salario_base}")


# Confirmar los datos ingresados 
    confirmacion = input(f"{CYAN}¿Son correctos estos datos? (si/no): {RESET_COLOR}").strip().lower()
    if confirmacion != 'si':
        print(f"{RED}-----------------------------------------------------------")
        print(f"Operación cancelada. Los datos no fueron guardados.{RESET_COLOR}")
        return


# Crear el directorio "datos" si no existe
    os.makedirs("datos", exist_ok=True)


# Definir la ruta del archivo de empleados
    archivo_empleados = "datos/empleados.txt"
    
# Abrir el archivo en modo append ('a') para agregar los datos del nuevo empleado
    with open(archivo_empleados, 'a') as file:
        file.write(f"ID del empleado: {id_empleado}\n")
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Puesto de trabajo: {puesto}\n")
        file.write(f"Sexo: {sexo}\n")
        file.write(f"Edad: {edad}\n")
        file.write(f"Teléfono: {telefono}\n")
        file.write(f"Correo electrónico: {correo}\n")
        file.write(f"Salario Base: {salario_base}\n")
        file.write("-----------------------------------------------------------") # Separador entre empleados


# Imprimir un mensaje de confirmación indicando que el empleado ha sido agregado
    print(f"{GREEN}-----------------------------------------------------------")
    print(f"Empleado {nombre} ha sido agregado a la planilla.{RESET_COLOR}")



# FUNCION 2: Eliminar Empleados
def eliminar_empleado():
    """
    Función para eliminar un empleado de la planilla basándose en su ID.
    Solicita el ID del empleado, verifica su existencia y lo elimina si se confirma.
    """
    
    # Mensaje Inicial 
    print(f"{MAGENTA}-----------------------------------------------------------")
    print("⦁ Ingrese el ID del empleado a eliminar:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")

    # Solicitar el ID del empleado
    while True:
        id_empleado = input(f"{CYAN}‣ ID del empleado: {RESET_COLOR}").strip()
        if not id_empleado:
            print(f"{RED}El ID del empleado no puede estar vacío.{RESET_COLOR}")
            continue
        break

    # Leer la lista actual de empleados
    empleados = leer_empleados()

    # Verificar que el empleado exista
    empleados_con_id = [emp for emp in empleados if emp['ID del empleado'] == id_empleado]
    if not empleados_con_id:
        print(f"{RED}-----------------------------------------------------------")
        print(f"No se encontró ningún empleado con el ID {id_empleado}.{RESET_COLOR}")
        return

    # Confirmar de eliminación
    while True:
        confirmacion = input(f"{CYAN}¿Está seguro que desea eliminar al empleado con ID {id_empleado}? (si/no): {RESET_COLOR}").strip().lower()
        if confirmacion in ['si', 'no']:
            break
        print(f"{RED}Por favor, ingrese 'si' o 'no'.{RESET_COLOR}")
    
    if confirmacion != 'si':
        print(f"{RED}-----------------------------------------------------------")
        print(f"Operación cancelada. El empleado no fue eliminado.{RESET_COLOR}")
        return
    
    # Filtrar la lista de empleados excluyendo al empleado que coincide con el ID ingresado
    empleados = [emp for emp in empleados if emp['ID del empleado'] != id_empleado]

    # Sobrescribir el archivo con la lista actualizada de empleados
    try:
        with open("datos/empleados.txt", 'w') as file:
            for emp in empleados:
                for key, value in emp.items():
                    file.write(f"{key}: {value}\n")
                file.write(f"{'-'*50}\n")
        # Imprimir un mensaje de confirmación indicando que el empleado ha sido eliminado
        print(f"{GREEN}-----------------------------------------------------------")
        print(f"Empleado con ID {id_empleado} ha sido eliminado de la planilla.{RESET_COLOR}")
    except Exception as e:
        print(f"{RED}Error al actualizar la lista de empleados: {str(e)}{RESET_COLOR}")



# FUNCION 3: Eliminar Empleados
def ver_lista_empleados():
    
    """
    Función para mostrar la lista de empleados.
    Lee la información de los empleados desde un archivo y la muestra en la consola.
    Permite generar un archivo de texto con la lista de empleados si se desea.
    """

# Leer la lista de empleados 
    empleados = leer_empleados()
    
    
# Verificar si la lista de empleados está vacía
    if not empleados:
        print(f"{RED}-----------------------------------------------------------")
        print(f"No hay empleados en la planilla.{RESET_COLOR}")
        return


# Mensaje Inicial 
    print(f"{MAGENTA}-----------------------------------------------------------")
    print("⦁ Lista de Empleados:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")


# Iterar sobre la lista de empleados y mostrar la información de cada uno
    for emp in empleados:
        print(f"ID del empleado:     {emp['ID del empleado']}")
        print(f"Nombre:              {emp['Nombre']}")
        print(f"Puesto de trabajo:   {emp['Puesto de trabajo']}")
        print(f"Sexo:                {emp['Sexo']}")
        print(f"Edad:                {emp['Edad']}")
        print(f"Teléfono:            {emp['Teléfono']}")
        print(f"Correo electrónico:  {emp['Correo electrónico']}")
        print(f"Salario Base:        {emp['Salario Base']}")
        print("-----------------------------------------------------------")


# Preguntar al usuario si desea generar un archivo con la lista de empleados
    while True:
        desea_generar_lista = input(f"{CYAN}‣ ¿Desea generar un archivo de lista de empleados? (si/no): {RESET_COLOR}").strip().lower()
        if desea_generar_lista in ['si', 'no']:
            break
        print(f"{RED}Por favor, ingrese 'si' o 'no'.{RESET_COLOR}")
    
#Conclucion de respuesta
    if desea_generar_lista == "si":
        try:
            generar_lista_empleados_txt(empleados)
            print(f"{GREEN}-----------------------------------------------------------")
            print(f"Archivo con la lista de empleados generado exitosamente.{RESET_COLOR}")
        except Exception as e:
            print(f"{RED}-----------------------------------------------------------")
            print(f"No se logro generar el archivo: {str(e)}{RESET_COLOR}")



# FUNCION 4: Buscar Empleado
def buscar_empleado():
    """
    Función para buscar un empleado por su ID.
    Lee la información de los empleados desde un archivo y muestra el empleado que coincide con el ID buscado.
    Permite generar un archivo de texto con la información del empleado si se desea.
    """
    print(f"{MAGENTA}-----------------------------------------------------------")
    print("Ingrese el ID del empleado a buscar:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    
    # Solicitar el ID del empleado con validación
    while True:
        id_empleado = input(f"{CYAN}‣ ID del empleado: {RESET_COLOR}").strip()
        if not id_empleado:
            print(f"{RED}El ID del empleado no puede estar vacío.{RESET_COLOR}")
            continue
        break
    
    # Leer la lista de empleados
    empleados = leer_empleados()
    
    # Buscar coincidencia por ID
    coincidencia = next((emp for emp in empleados if emp['ID del empleado'] == id_empleado), None)

    # Si no hay coincidencia, mostrar mensaje y salir
    if not coincidencia:
        print(f"{RED}-----------------------------------------------------------")
        print(f"No se encontró ningún empleado con el ID {id_empleado}.")
        print("Por favor, revise el ID ingresado y vuelva a intentarlo.")
        print(f"-----------------------------------------------------------{RESET_COLOR}")
        return

    # Mostrar la coincidencia encontrada
    print(f"{MAGENTA}-----------------------------------------------------------")
    print(f"Se encontró el siguiente empleado:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    for key, value in coincidencia.items():
        print(f"{key}: {value}")
    print("-----------------------------------------------------------}")
    
    # Preguntar si se desea generar un archivo con la información del empleado
    while True:
        desea_generar_info = input(f"{CYAN}‣ ¿Desea generar un archivo con la información del empleado? (si/no): {RESET_COLOR}").strip().lower()
        if desea_generar_info in ['si', 'no']:
            break
        print(f"{RED}Por favor, ingrese 'si' o 'no'.{RESET_COLOR}")
    
    # Generar el archivo si la respuesta es 'si'
    if desea_generar_info == "si":
        try:
            generar_empleado_info_txt(coincidencia)
            print(f"{GREEN}-----------------------------------------------------------")
            print(f"Archivo con la información del empleado generado exitosamente.{RESET_COLOR}")
        except Exception as e:
            print(f"{RED}-----------------------------------------------------------")
            print(f"No se logro generar el archivo: {str(e)}{RESET_COLOR}")
