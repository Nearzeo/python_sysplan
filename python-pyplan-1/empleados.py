# empleados.py
import datetime
from utils import generar_recibo_txt, generar_lista_empleados_txt, generar_empleado_info_txt, RESET_COLOR, BRIGHT, GREEN, RED, YELLOW

empleados = {}

def ingresar_empleado():
    print(f"{GREEN}-----------------------------------------------------------")
    print("Ingrese los datos del nuevo empleado:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    id_empleado = input(f"{YELLOW}‣ ID del empleado: {RESET_COLOR}").strip()
    nombre = input(f"{YELLOW}‣ Nombre del empleado: {RESET_COLOR}").strip()
    if id_empleado in empleados:
        print(f"{RED}El empleado ya existe en la planilla.{RESET_COLOR}")
        return

    puesto = input(f"{YELLOW}‣ Puesto de trabajo: {RESET_COLOR}").strip()
    sexo = input(f"{YELLOW}‣ Sexo (m/f): {RESET_COLOR}").strip()
    edad = int(input(f"{YELLOW}‣ Edad: {RESET_COLOR}").strip())
    telefono = input(f"{YELLOW}‣ Teléfono: {RESET_COLOR}").strip()
    correo = input(f"{YELLOW}‣ Correo electrónico: {RESET_COLOR}").strip()
    salario_base = float(input(f"{YELLOW}‣ Salario Base: {RESET_COLOR}").strip())
    print(f"{GREEN}-----------------------------------------------------------{RESET_COLOR}")

    empleados[id_empleado] = {
        'nombre': nombre,
        'puesto': puesto,
        'sexo': sexo,
        'edad': edad,
        'telefono': telefono,
        'correo': correo,
        'salario_base': salario_base
    }

    print(f"{GREEN}Empleado {nombre} ha sido agregado a la planilla.{RESET_COLOR}")

def eliminar_empleado():
    print(f"{GREEN}-----------------------------------------------------------")
    print("⦁ Ingrese el ID del empleado a eliminar:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    id_empleado = input(f"{YELLOW}‣ ID del empleado: {RESET_COLOR}").strip()
    nombre = input(f"{YELLOW}‣ Nombre del empleado: {RESET_COLOR}").strip()
    if id_empleado not in empleados or empleados[id_empleado]['nombre'] != nombre:
        print(f"{RED}-----------------------------------------------------------")
        print("El empleado no existe en la planilla o los datos no coinciden.")
        print("-----------------------------------------------------------{RESET_COLOR}")
        return

    confirmacion = input(f"{YELLOW}¿Está seguro que desea eliminar a {nombre} de la planilla? (si/no): {RESET_COLOR}").strip().lower()
    if confirmacion == "si":
        del empleados[id_empleado]
        print(f"{GREEN}Empleado {nombre} ha sido eliminado de la planilla.{RESET_COLOR}")
    else:
        print(f"{RED}-----------------------------------------------------------")
        print("Operación cancelada.")
        print("-----------------------------------------------------------{RESET_COLOR}")

def ver_lista_empleados():
    if not empleados:
        print(f"{RED}-----------------------------------------------------------")
        print("No hay empleados en la planilla.")
        print("-----------------------------------------------------------{RESET_COLOR}")
        return

    print(f"{GREEN}-----------------------------------------------------------")
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

    desea_generar_lista = input(f"{YELLOW}‣ ¿Desea generar un archivo de lista de empleados? (si/no): {RESET_COLOR}").strip().lower()
    if desea_generar_lista == "si":
        generar_lista_empleados_txt(empleados)

def buscar_empleado():
    print(f"{GREEN}-----------------------------------------------------------")
    print("Ingrese el nombre del empleado a buscar:")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    nombre = input(f"{YELLOW}‣ Nombre del empleado: {RESET_COLOR}").strip()
    coincidencias = [info for info in empleados.values() if nombre.lower() in info['nombre'].lower()]

    if not coincidencias:
        print(f"{RED}-----------------------------------------------------------")
        print("No se encontraron coincidencias.")
        print("-----------------------------------------------------------{RESET_COLOR}")
        return

    print(f"{GREEN}-----------------------------------------------------------")
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

    desea_generar_info = input(f"{YELLOW}‣ ¿Desea generar un archivo con la información del empleado? (si/no): {RESET_COLOR}").strip().lower()
    if desea_generar_info == "si":
        for info in coincidencias:
            generar_empleado_info_txt(info)
