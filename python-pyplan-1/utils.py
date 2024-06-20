# utils.py
import re
import datetime

RESET_COLOR = '\033[0m'
BRIGHT = '\033[1m'

# Usar códigos RGB con ANSI 24-bit
def rgb_to_ansi(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

RED = rgb_to_ansi(243, 139, 168)
GREEN = rgb_to_ansi(166, 227, 161)
YELLOW = rgb_to_ansi(249, 226, 175)
BLUE = rgb_to_ansi(137, 180, 250)
MAGENTA = rgb_to_ansi(203, 166, 247)  
CYAN = rgb_to_ansi(148, 226, 213)
WHITE = '\033[37m'

def generar_recibo_txt(nombre, salario_bruto, isss, afp, renta, deducciones_totales, salario_neto):
    archivo_txt = f"{nombre}_recibo.txt"
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo_txt, "w") as file:
        file.write("Recibo de Pago\n")                                              #Escribe el encabezado del recibo.
        file.write(f"Fecha y Hora: {fecha_actual}\n")
        file.write(f"\nEmpleado:\n{nombre}\n")                                      #Escribe el nombre del empleado.
        file.write(f"\nSalario Bruto:             ${salario_bruto:.2f}\n")          #Escribe el sueldo bruta.
        file.write(f"\nISSS:                      ${isss:.2f}\n")                   #Escribe la deduccion de ISSS.
        file.write(f"AFP:                       ${afp:.2f}\n")                      #Escribe la deduccion de AFP.
        file.write(f"Renta:                     ${renta:.2f}\n")                    #Escribe la deduccion de renta.
        file.write(f"Deducciones Totales:       ${deducciones_totales:.2f}\n")      #Escribe las deducciones totales.
        file.write(f"\nSalario Neto:              ${salario_neto:.2f}\n")           #Escribe el sueldo neto.
    print(f"{GREEN}◆ Recibo generado: {archivo_txt}{RESET_COLOR}")

def generar_lista_empleados_txt(empleados):
    archivo_txt = "lista_empleados.txt"
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo_txt, "w") as file:
        file.write("Lista de Empleados\n")
        file.write(f"Fecha y Hora: {fecha_actual}\n")
        file.write("-----------------------------------------------------------\n")
        for id_empleado, info in empleados.items():
            file.write(f"\nID: {id_empleado}\n")
            file.write(f"  Nombre: {info['nombre']}\n")
            file.write(f"  Puesto: {info['puesto']}\n")
            file.write(f"  Sexo: {info['sexo']}\n")
            file.write(f"  Edad: {info['edad']}\n")
            file.write(f"  Teléfono: {info['telefono']}\n")
            file.write(f"  Correo: {info['correo']}\n")
            file.write(f"  Salario Base: ${info['salario_base']:.2f}\n")
        file.write("-----------------------------------------------------------\n")
    print(f"{GREEN}◆ Lista de empleados generada: {archivo_txt}{RESET_COLOR}")

def generar_empleado_info_txt(info):
    archivo_txt = f"{info['nombre']}_info.txt"
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo_txt, "w") as file:
        file.write("Información del Empleado\n")
        file.write(f"Fecha y Hora: {fecha_actual}\n")
        file.write("-----------------------------------------------------------\n")
        file.write(f"Nombre: {info['nombre']}\n")
        file.write(f"Puesto: {info['puesto']}\n")
        file.write(f"Sexo: {info['sexo']}\n")
        file.write(f"Edad: {info['edad']}\n")
        file.write(f"Teléfono: {info['telefono']}\n")
        file.write(f"Correo: {info['correo']}\n")
        file.write(f"Salario Base: ${info['salario_base']:.2f}\n")
        file.write("-----------------------------------------------------------\n")
    print(f"{GREEN}◆ Información del empleado generada: {archivo_txt}{RESET_COLOR}")

def validar_correo(correo):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, correo) is not None