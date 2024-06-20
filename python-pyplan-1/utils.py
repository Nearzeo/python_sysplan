import datetime
import re
import os
from pathlib import Path

# Constantes de colores y estilos
RESET_COLOR = '\033[0m'
BRIGHT = '\033[1m'

def rgb_to_ansi(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

# Definición de colores
RED = rgb_to_ansi(255, 69, 69)
GREEN = rgb_to_ansi(0, 255, 127)
YELLOW = rgb_to_ansi(255, 255, 28)
BLUE = rgb_to_ansi(30, 144, 255)
MAGENTA = rgb_to_ansi(183, 166, 246)
CYAN = rgb_to_ansi(199, 255, 237)
WHITE = '\033[37m'

# Ruta del archivo de empleados
EMPLEADOS_FILE_PATH = Path("datos/empleados.txt")

def validar_correo(correo):
    """
    Valida el formato del correo electrónico.
    """
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, correo) is not None

def leer_empleados():
    """
    Lee el archivo de empleados y devuelve una lista de diccionarios con la información de cada empleado.
    """
    empleados = []
    if EMPLEADOS_FILE_PATH.exists():
        try:
            with EMPLEADOS_FILE_PATH.open("r") as file:
                empleado = {}
                for line in file:
                    line = line.strip()
                    if line == "-" * 59:
                        if empleado:
                            empleados.append(empleado)
                        empleado = {}
                    elif ":" in line:
                        key, value = line.split(":", 1)
                        empleado[key.strip()] = value.strip()
        except Exception as e:
            print(f"{RED}Error al leer el archivo de empleados: {str(e)}{RESET_COLOR}")
    return empleados

def generar_recibo_txt(nombre, salario_bruto, isss, afp, renta, deducciones_totales, salario_neto):
    """
    Genera un archivo de texto con el recibo de pago de un empleado.
    """
    archivo_txt = f"{nombre}_recibo.txt"
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(archivo_txt, "w") as file:
            file.write("Recibo de Pago\n")
            file.write(f"Fecha y Hora: {fecha_actual}\n")
            file.write(f"\nEmpleado:\n{nombre}\n")
            file.write(f"\nSalario Bruto:             ${salario_bruto:.2f}\n")
            file.write(f"\nISSS:                      ${isss:.2f}\n")
            file.write(f"AFP:                       ${afp:.2f}\n")
            file.write(f"Renta:                     ${renta:.2f}\n")
            file.write(f"Deducciones Totales:       ${deducciones_totales:.2f}\n")
            file.write(f"\nSalario Neto:              ${salario_neto:.2f}\n")
        print(f"{GREEN}◆ Recibo generado: {archivo_txt}{RESET_COLOR}")
    except Exception as e:
        print(f"{RED}Error al generar el recibo: {str(e)}{RESET_COLOR}")

def generar_lista_empleados_txt(empleados):
    """
    Genera un archivo de texto con la lista completa de empleados.
    """
    archivo_txt = "lista_empleados.txt"
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(archivo_txt, "w") as file:
            file.write("Lista de Empleados\n")
            file.write(f"Fecha y Hora: {fecha_actual}\n")
            file.write("-----------------------------------------------------------\n")
            for empleado in empleados:
                for key, value in empleado.items():
                    file.write(f"{key}: {value}\n")
                file.write("-----------------------------------------------------------\n")
        print(f"{GREEN}◆ Lista de empleados generada: {archivo_txt}{RESET_COLOR}")
    except Exception as e:
        print(f"{RED}Error al generar la lista de empleados: {str(e)}{RESET_COLOR}")

def generar_empleado_info_txt(info):
    """
    Genera un archivo de texto con la información detallada de un empleado.
    """
    archivo_txt = f"{info['ID del empleado']}_info.txt"
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(archivo_txt, "w") as file:
            file.write("Información del Empleado\n")
            file.write(f"Fecha y Hora: {fecha_actual}\n")
            file.write("-----------------------------------------------------------\n")
            for key, value in info.items():
                file.write(f"{key}: {value}\n")
            file.write("-----------------------------------------------------------\n")
        print(f"{GREEN}◆ Información del empleado generada: {archivo_txt}{RESET_COLOR}")
    except Exception as e:
        print(f"{RED}Error al generar la información del empleado: {str(e)}{RESET_COLOR}")
