from welcome import imprimir_bienvenida
from empleados import ingresar_empleado, eliminar_empleado, ver_lista_empleados, buscar_empleado
from calculos import calcular_tarifa_hora, calcular_salario_hora_extra, calcular_salario_bruto, calcular_deducciones, calcular_salario_neto
from utils import leer_empleados, generar_recibo_txt, RESET_COLOR, BLUE, MAGENTA, RED, CYAN, MAGENTA

def mostrar_menu_principal():
    """
    Muestra el menú principal del sistema.
    """
    print(f"{BLUE}\n-----------------------------------------------------------")
    print("Bienvenido al Sistema de Planillas")
    print(f"-----------------------------------------------------------{RESET_COLOR}")
    print(f"{MAGENTA}⦁ Menú Principal:")
    print("1. Ingresar Empleado a la Planilla")
    print("2. Calcular Salario")
    print("3. Eliminar Empleado de la Planilla")
    print("4. Ver Lista de Empleados")
    print("5. Buscar Empleado")
    print(f"6. Salir {RESET_COLOR}")

def validar_opcion(opcion, opciones_validas):
    """
    Valida que la opción ingresada por el usuario esté dentro de las opciones válidas.

    :param opcion: La opción ingresada por el usuario.
    :param opciones_validas: Lista de opciones válidas.
    :return: True si la opción es válida, False en caso contrario.
    """
    return opcion in opciones_validas

def obtener_float(mensaje):
    """
    Solicita al usuario que ingrese un valor flotante.

    :param mensaje: Mensaje para solicitar la entrada del usuario.
    :return: El valor flotante ingresado por el usuario.
    """
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print(f"{RED}Por favor, ingrese un número válido.{RESET_COLOR}")

def obtener_int(mensaje):
    """
    Solicita al usuario que ingrese un valor entero.

    :param mensaje: Mensaje para solicitar la entrada del usuario.
    :return: El valor entero ingresado por el usuario.
    """
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print(f"{RED}Por favor, ingrese un número entero válido.{RESET_COLOR}")

def seleccionar_tipo_horas_extras():
    """
    Permite al usuario seleccionar el tipo de horas extras y retorna el tipo seleccionado.

    :return: Tipo de horas extras seleccionadas.
    """
    while True:
        print(f"{MAGENTA}-----------------------------------------------------------")
        print("⦁ Tipos de Horas Extras:")
        print("1. Diurnas")
        print("2. Nocturnas")
        print("3. Día de Descanso")
        print("4. Asueto")
        print(f"-----------------------------------------------------------{RESET_COLOR}")

        tipo_principal = obtener_int(f"{CYAN}‣ Seleccione el tipo de horas extras: {RESET_COLOR}")
        if tipo_principal == 1:
            return 1
        elif tipo_principal == 2:
            return 2
        elif tipo_principal == 3:
            print(f"{MAGENTA}-----------------------------------------------------------")
            print("1. Diurnas\n2. Nocturnas")
            print(f"-----------------------------------------------------------{RESET_COLOR}")
            tipo_secundario = obtener_int(f"{CYAN}‣ Seleccione el tipo específico de horas extras en Día de Descanso: {RESET_COLOR}")
            if tipo_secundario in [1, 2]:
                return 3 if tipo_secundario == 1 else 4
        elif tipo_principal == 4:
            print(f"{MAGENTA}-----------------------------------------------------------")
            print("1. Diurnas\n2. Nocturnas")
            print(f"-----------------------------------------------------------{RESET_COLOR}")
            tipo_secundario = obtener_int(f"{CYAN}‣ Seleccione el tipo específico de horas extras en Asueto: {RESET_COLOR}")
            if tipo_secundario in [1, 2]:
                return 5 if tipo_secundario == 1 else 6

        print(f"{RED}-----------------------------------------------------------")
        print("Opción no válida. Por favor, seleccione una opción del menú.")
        print(f"-----------------------------------------------------------{RESET_COLOR}")

def obtener_input_validado(mensaje, validacion):
    """
    Solicita al usuario que ingrese un valor y valida la entrada usando una función de validación.

    :param mensaje: Mensaje para solicitar la entrada del usuario.
    :param validacion: Función de validación que debe retornar True si la entrada es válida.
    :return: El valor ingresado por el usuario.
    """
    while True:
        valor = input(mensaje).strip()
        if validacion(valor):
            return valor
        print(f"{RED}Entrada no válida. Por favor, inténtelo de nuevo.{RESET_COLOR}")

def validar_no_vacio(valor):
    """
    Valida que una cadena de texto no esté vacía.

    :param valor: Cadena de texto a validar.
    :return: True si la cadena no está vacía, False en caso contrario.
    """
    return bool(valor)

def validar_si_no(valor):
    """
    Valida que una cadena de texto sea 'si' o 'no'.

    :param valor: Cadena de texto a validar.
    :return: True si la cadena es 'si' o 'no', False en caso contrario.
    """
    return valor in ['si', 'no']

if __name__ == "__main__":
    imprimir_bienvenida()
    while True:
        mostrar_menu_principal()
        opcion = input(f"{CYAN}‣ Seleccione una opción: {RESET_COLOR}").strip()
        
        if not validar_opcion(opcion, ["1", "2", "3", "4", "5", "6"]):
            print(f"{RED}-----------------------------------------------------------")
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            print(f"-----------------------------------------------------------{RESET_COLOR}")
            continue

        if opcion == "1":
            ingresar_empleado()
        elif opcion == "2":
            print(f"{MAGENTA}-----------------------------------------------------------")
            print("‣ Ingrese los siguientes datos: \n(Recuerde que el sistema está diseñado para calcular el sueldo neto mensual.)")
            print(f"-----------------------------------------------------------{RESET_COLOR}")

            id_empleado = obtener_input_validado(f"{CYAN}‣ ID del empleado: {RESET_COLOR}", validar_no_vacio)
            nombre = obtener_input_validado(f"{CYAN}‣ Nombre del empleado: {RESET_COLOR}", validar_no_vacio)
            empleados = leer_empleados()
            empleado = next((emp for emp in empleados if emp['ID del empleado'].strip() == id_empleado and emp['Nombre'].strip() == nombre), None)
            
            if not empleado:
                print(f"{RED}-----------------------------------------------------------")
                print("El empleado no existe en la planilla o los datos no coinciden.")
                print(f"-----------------------------------------------------------{RESET_COLOR}")
                continue

            salario_base = float(empleado['Salario Base'])

            total_horas_extras = 0
            desea_horas_extras = obtener_input_validado(f"{CYAN}‣ ¿Desea ingresar horas extras? (si/no): {RESET_COLOR}", validar_si_no).lower()
            while desea_horas_extras == "si":
                tipo_horas_extras = seleccionar_tipo_horas_extras()
                horas_extras = obtener_float(f"{CYAN}‣ Horas Extras Trabajadas: {RESET_COLOR}")
                total_horas_extras += horas_extras
                desea_horas_extras = obtener_input_validado(f"{CYAN}‣ ¿Desea ingresar más horas extras? (si/no): {RESET_COLOR}", validar_si_no).lower()

            bonificaciones = obtener_float(f"{CYAN}‣ Bonificaciones: {RESET_COLOR}")
            comisiones = obtener_float(f"{CYAN}‣ Comisiones: {RESET_COLOR}")

            tarifa_hora = calcular_tarifa_hora(salario_base)
            salario_hora_extra = calcular_salario_hora_extra(tarifa_hora, tipo_horas_extras, total_horas_extras)
            salario_bruto = calcular_salario_bruto(salario_base, salario_hora_extra, bonificaciones, comisiones)
            isss, afp, renta, deducciones_totales = calcular_deducciones(salario_bruto)
            salario_neto = calcular_salario_neto(salario_bruto, deducciones_totales)

            print(f"{MAGENTA}-----------------------------------------------------------")
            print("⦁ Información de Pago")
            print(f"⦁ Empleado: {nombre} ")
            print(f"⦁ Salario Bruto:             ${salario_bruto:.2f}")
            print(f"⦁ ISSS:                      ${isss:.2f}")
            print(f"⦁ AFP:                       ${afp:.2f}")
            print(f"⦁ Renta:                     ${renta:.2f}")
            print(f"⦁ Deducciones Totales:       ${deducciones_totales:.2f}")
            print(f"⦁ Salario Neto:              ${salario_neto:.2f}")
            print(f"-----------------------------------------------------------{RESET_COLOR}")

            desea_generar_recibo = obtener_input_validado(f"{CYAN}‣ ¿Desea generar un archivo de recibo? (si/no): {RESET_COLOR}", validar_si_no).lower()
            if desea_generar_recibo == "si":
                generar_recibo_txt(nombre, salario_bruto, isss, afp, renta, deducciones_totales, salario_neto)
        elif opcion == "3":
            eliminar_empleado()
        elif opcion == "4":
            ver_lista_empleados()
        elif opcion == "5":
            buscar_empleado()
        elif opcion == "6":
            print(f"{MAGENTA}-----------------------------------------------------------")
            print("Gracias por usar el sistema de nóminas. ¡Hasta luego!")
            print(f"-----------------------------------------------------------{RESET_COLOR}")
            break