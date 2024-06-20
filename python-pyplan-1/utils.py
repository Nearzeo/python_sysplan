import datetime
import re
import os

RESET_COLOR = '\033[0m'
BRIGHT = '\033[1m'

# Usar códigos RGB con ANSI 24-bit
def rgb_to_ansi(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

RED = rgb_to_ansi(255, 69, 69)
GREEN = rgb_to_ansi(0, 255, 127)
YELLOW = rgb_to_ansi(255, 255, 28)
BLUE = rgb_to_ansi(30, 144, 255)
MAGENTA = rgb_to_ansi(183, 166, 246)
CYAN = rgb_to_ansi(199, 255, 237)
WHITE = '\033[37m'

def validar_correo(correo):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, correo) is not None

def leer_empleados():
    """
    Lee el archivo de empleados y devuelve una lista de diccionarios con la información de cada empleado.
    """
    empleados = []
    if os.path.exists("datos/empleados.txt"):
        with open("datos/empleados.txt", "r") as file:
            empleado = {}
            for line in file:
                line = line.strip()
                if line == "-" * 50:
                    if empleado:
                        empleados.append(empleado)
                    empleado = {}
                elif ":" in line:
                    key, value = line.split(":", 1)
                    empleado[key.strip()] = value.strip()
    return empleados

def generar_recibo_txt(nombre, salario_bruto, isss, afp, renta, deducciones_totales, salario_neto):
    archivo_txt = f"{nombre}_recibo.txt"
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

def generar_lista_empleados_txt(empleados):
    archivo_txt = "lista_empleados.txt"
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo_txt, "w") as file:
        file.write("Lista de Empleados\n")
        file.write(f"Fecha y Hora: {fecha_actual}\n")
        file.write("-----------------------------------------------------------\n")
        for empleado in empleados:
            for key, value in empleado.items():
                file.write(f"{key}: {value}\n")
            file.write("-----------------------------------------------------------\n")
    print(f"{GREEN}◆ Lista de empleados generada: {archivo_txt}{RESET_COLOR}")

def generar_empleado_info_txt(info):
    archivo_txt = f"{info['ID del empleado']}_info.txt"
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo_txt, "w") as file:
        file.write("Información del Empleado\n")
        file.write(f"Fecha y Hora: {fecha_actual}\n")
        file.write("-----------------------------------------------------------\n")
        for key, value in info.items():
            file.write(f"{key}: {value}\n")
        file.write("-----------------------------------------------------------\n")
    print(f"{GREEN}◆ Información del empleado generada: {archivo_txt}{RESET_COLOR}")
