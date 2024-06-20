# Modulo empleados.py

# Importaciones
import re # permite buscar coincidencias.
import datetime # permite trabajar con fecha 

# Modulo utils.py
from utils import generar_lista_empleados_txt, generar_empleado_info_txt, validar_correo, RESET_COLOR, MAGENTA, RED, CYAN, GREEN

#Diccionario 'empleados' Vacio
empleados = {}

#def 1: Nuevos Empleados
def ingresar_empleado():

# Función para ingresar un nuevo empleado al diccionario 'empleados'.
# Solicita los datos del empleado y los valida antes de almacenarlos.
    
# Mensaje Inicial
    print(f"{MAGENTA}-----------------------------------------------------------")
    print("Ingrese los datos del nuevo empleado:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    
# Solicitar y validar el ID del empleado
    while True:
        id_empleado = input(f"{CYAN}‣ ID del empleado: {RESET_COLOR}").strip()
        if not id_empleado:
            print(f"{RED}El ID del empleado no puede estar vacío.{RESET_COLOR}")
            continue
        elif id_empleado in empleados:
            print(f"{RED}Ya existe un empleado con ese ID.{RESET_COLOR}")
            return
        break
        
# Solicitar el nombre del empleado 
    while True:
        nombre = input(f"{CYAN}‣ Nombre del empleado: {RESET_COLOR}").strip()
        if not nombre:
            print(f"{RED}El nombre del empleado no puede estar vacío.{RESET_COLOR}")
            continue
        break

# Solicitar el puesto de trabajo del empleado
    while True:
        puesto = input(f"{CYAN}‣ Puesto de trabajo: {RESET_COLOR}").strip()
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
    
# Agregar el nuevo empleado al diccionario
    empleados[id_empleado] = {
        'nombre': nombre,
        'puesto': puesto,
        'sexo': sexo,
        'edad': edad,
        'telefono': telefono,
        'correo': correo,
        'salario_base': salario_base
    }
    
    print(f"{GREEN}-----------------------------------------------------------")
    print(f"Empleado {nombre} ha sido agregado a la planilla.{RESET_COLOR}")


#def 2: Eliminar Empleados
def eliminar_empleado():
    print(f"{MAGENTA}-----------------------------------------------------------")
    print("⦁ Ingrese el ID del empleado a eliminar:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    id_empleado = input(f"{CYAN}‣ ID del empleado: {RESET_COLOR}").strip()
    nombre = input(f"{CYAN}‣ Nombre del empleado: {RESET_COLOR}").strip()
    if id_empleado not in empleados or empleados[id_empleado]['nombre'] != nombre:
        print(f"{RED}-----------------------------------------------------------")
        print("El empleado no existe en la planilla o los datos no coinciden.")
        print("-----------------------------------------------------------{RESET_COLOR}")
        return

    confirmacion = input(f"{CYAN}¿Está seguro que desea eliminar a {nombre} de la planilla? (si/no): {RESET_COLOR}").strip().lower()
    if confirmacion == "si":
        del empleados[id_empleado]
        print(f"{MAGENTA}Empleado {nombre} ha sido eliminado de la planilla.{RESET_COLOR}")
    else:
        print(f"{RED}-----------------------------------------------------------")
        print("Operación cancelada.")
        print("-----------------------------------------------------------{RESET_COLOR}")


#def 3:
def ver_lista_empleados():
    if not empleados:
        print(f"{RED}-----------------------------------------------------------")
        print("No hay empleados en la planilla.")
        print("-----------------------------------------------------------{RESET_COLOR}")
        return

    print(f"{MAGENTA}-----------------------------------------------------------")
    print("⦁ Lista de Empleados:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    for id_empleado, info in empleados.items():
        print(f"\nID: {id_empleado}")
        print(f"  Nombre: {info['nombre']}")
        print(f"  Puesto: {info['puesto']}")
        print(f"  Sexo: {info['sexo']}")
        print(f"  Edad: {info['edad']}")
        print(f"  Teléfono: {info['telefono']}")
        print(f"  Correo: {info['correo']}")
        print(f"  Salario Base: ${info['salario_base']:.2f}")

    desea_generar_lista = input(f"{CYAN}‣ ¿Desea generar un archivo de lista de empleados? (si/no): {RESET_COLOR}").strip().lower()
    if desea_generar_lista == "si":
        generar_lista_empleados_txt(empleados)


#def 4:
def buscar_empleado():
    print(f"{MAGENTA}-----------------------------------------------------------")
    print("Ingrese el nombre del empleado a buscar:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    nombre = input(f"{CYAN}‣ Nombre del empleado: {RESET_COLOR}").strip()
    coincidencias = [info for info in empleados.values() if nombre.lower() in info['nombre'].lower()]

    if not coincidencias:
        print(f"{RED}-----------------------------------------------------------")
        print("No se encontraron coincidencias.")
        print("-----------------------------------------------------------{RESET_COLOR}")
        return

    print(f"{MAGENTA}-----------------------------------------------------------")
    print(f"Se encontraron {len(coincidencias)} coincidencias:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    for info in coincidencias:
        print(f"\nNombre: {info['nombre']}")
        print(f"  Puesto: {info['puesto']}")
        print(f"  Sexo: {info['sexo']}")
        print(f"  Edad: {info['edad']}")
        print(f"  Teléfono: {info['telefono']}")
        print(f"  Correo: {info['correo']}")
        print(f"  Salario Base: ${info['salario_base']:.2f}")

    desea_generar_info = input(f"{CYAN}‣ ¿Desea generar un archivo con la información del empleado? (si/no): {RESET_COLOR}").strip().lower()
    if desea_generar_info == "si":
        for info in coincidencias:
            generar_empleado_info_txt(info)