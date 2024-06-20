# alfa.py
import datetime
from welcome import imprimir_bienvenida
from empleados import ingresar_empleado, eliminar_empleado, ver_lista_empleados, buscar_empleado, empleados
from calculos import calcular_tarifa_hora, calcular_salario_hora_extra, calcular_salario_bruto, calcular_deducciones, calcular_salario_neto
from utils import generar_recibo_txt, RESET_COLOR, BRIGHT, BLUE, MAGENTA, RED, CYAN
def mostrar_menu_principal():
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

if __name__ == "__main__":
    imprimir_bienvenida()
    while True:
        mostrar_menu_principal()
        opcion = input(f"{CYAN}‣ Seleccione una opción: {RESET_COLOR}").strip()
        if opcion == "1":
            ingresar_empleado()
        elif opcion == "2":
            print(f"{MAGENTA}-----------------------------------------------------------")
            print("‣ Ingrese los siguientes datos: \n(Recuerde que el sistema está diseñado para calcular el sueldo neto mensual.)")
            print(f"-----------------------------------------------------------{RESET_COLOR}")
            id_empleado = input(f"{CYAN}‣ ID del empleado: {RESET_COLOR}").strip()
            nombre = input(f"{CYAN}‣ Nombre del empleado: {RESET_COLOR}").strip()
            if id_empleado not in empleados or empleados[id_empleado]['nombre'] != nombre:
                print(f"{RED}-----------------------------------------------------------")
                print("El empleado no existe en la planilla o los datos no coinciden.")
                print("-----------------------------------------------------------{RESET_COLOR}")
                continue

            empleado = empleados[id_empleado]
            salario_base = empleado['salario_base']

            total_horas_extras = 0
            tipo_horas_extras = 0
            desea_horas_extras = input(f"{CYAN}‣ ¿Desea ingresar horas extras? (si/no): {RESET_COLOR}").strip().lower()
            while desea_horas_extras == "si":
                print(f"{MAGENTA}-----------------------------------------------------------")
                print("⦁ Tipos de Horas Extras:")
                print("1. Diurnas")
                print("2. Nocturnas")
                print("3. Día de Descanso")
                print("4. Asueto")
                print(f"-----------------------------------------------------------{RESET_COLOR}")

                tipo_principal = int(input(f"{CYAN}‣ Seleccione el tipo de horas extras: {RESET_COLOR}").strip())
                if tipo_principal == 1:
                    tipo_horas_extras = 1
                elif tipo_principal == 2:
                    tipo_horas_extras = 2
                elif tipo_principal == 3:
                    print(f"{MAGENTA}-----------------------------------------------------------")
                    print("1. Diurnas\n2. Nocturnas")
                    print(f"-----------------------------------------------------------{RESET_COLOR}")
                    tipo_secundario = int(input(f"{CYAN}‣ Seleccione el tipo específico de horas extras en Día de Descanso: {RESET_COLOR}").strip())
                    if tipo_secundario == 1:
                        tipo_horas_extras = 3
                    elif tipo_secundario == 2:
                        tipo_horas_extras = 4
                    else:
                        print(f"{RED}-----------------------------------------------------------")
                        print("Opción no válida. Por favor, seleccione una opción del menú.")
                        print("-----------------------------------------------------------{RESET_COLOR}")
                        continue
                elif tipo_principal == 4:
                    print(f"{MAGENTA}-----------------------------------------------------------")
                    print("1. Diurnas\n2. Nocturnas")
                    print(f"-----------------------------------------------------------{RESET_COLOR}")
                    tipo_secundario = int(input(f"{CYAN}‣ Seleccione el tipo específico de horas extras en Asueto: {RESET_COLOR}").strip())
                    if tipo_secundario == 1:
                        tipo_horas_extras = 5
                    elif tipo_secundario == 2:
                        tipo_horas_extras = 6
                    else:
                        print(f"{RED}-------------------------------------------------------------------------------------")
                        print("Opción no válida. Por favor, seleccione una opción del menú.")
                        print("-------------------------------------------------------------------------------------{RESET_COLOR}")
                        continue
                else:
                    print(f"{RED}-------------------------------------------------------------------------------------")
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
                    print("-------------------------------------------------------------------------------------{RESET_COLOR}")
                    continue

                horas_extras = float(input(f"{CYAN}‣ Horas Extras Trabajadas: {RESET_COLOR}").strip())
                total_horas_extras += horas_extras
                desea_horas_extras = input(f"{CYAN}‣ ¿Desea ingresar más horas extras? (si/no): {RESET_COLOR}").strip().lower()

            bonificaciones = float(input(f"{CYAN}‣ Bonificaciones: {RESET_COLOR}").strip())
            comisiones = float(input(f"{CYAN}‣ Comisiones: {RESET_COLOR}").strip())

            tarifa_hora = calcular_tarifa_hora(salario_base)
            salario_hora_extra = calcular_salario_hora_extra(tarifa_hora, tipo_horas_extras, total_horas_extras)
            salario_bruto = calcular_salario_bruto(salario_base, salario_hora_extra, bonificaciones, comisiones)
            isss, afp, renta, deducciones_totales = calcular_deducciones(salario_bruto)
            salario_neto = calcular_salario_neto(salario_bruto, deducciones_totales)

            print(f"{MAGENTA}------------------------------------------------------------------------------------")
            print("⦁ Información de Pago")
            print(f"⦁ Empleado: {nombre} ")
            print(f"⦁ Salario Bruto:             ${salario_bruto:.2f}")
            print(f"⦁ ISSS:                      ${isss:.2f}")
            print(f"⦁ AFP:                       ${afp:.2f}")
            print(f"⦁ Renta:                     ${renta:.2f}")
            print(f"⦁ Deducciones Totales:       ${deducciones_totales:.2f}")
            print(f"⦁ Salario Neto:              ${salario_neto:.2f}")
            print(f"------------------------------------------------------------------------------------{RESET_COLOR}")

            desea_generar_recibo = input(f"{CYAN}‣ ¿Desea generar un archivo de recibo? (si/no): {RESET_COLOR}").strip().lower()
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
        else:
            print(f"{RED}-----------------------------------------------------------")
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            print(f"-----------------------------------------------------------{RESET_COLOR}")