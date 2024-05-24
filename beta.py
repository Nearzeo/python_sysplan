# Sistema de Planillas
import datetime
#
# Funciones
# Muestra el menu principal del sistema.
def mostrar_menu_principal():
    print("\n----------------------------------")
    print("Bienvenido al Sistema de Planillas")
    print("----------------------------------")    
    print("⦁ Menú Principal:")
    print("1. Calcular Salario")
    print("2. Salir")
#
#
# Calcula la tarifa por hora, suponiendo que se trabaje 22 dias al mes y 8 horas por semana.
def calcular_tarifa_hora(salario_base):
    return salario_base / 22 / 8
#
#
# Calcula el salario por hora extra. Varia segun el tipo de horas extras
def calcular_salario_hora_extra(tarifa_hora, tipo_horas_extras, horas_extras):
    if tipo_horas_extras == 1:
        return tarifa_hora * horas_extras * 2  # 100% de regargo
    elif tipo_horas_extras == 2:
        return tarifa_hora * horas_extras * 2.5  # 150% de regargo
    elif tipo_horas_extras == 3:
        return tarifa_hora * horas_extras * 4  # 300% de regargo
    elif tipo_horas_extras == 4:
        return tarifa_hora * horas_extras * 4.75  # 375% de regargo
    elif tipo_horas_extras == 5:
        return tarifa_hora * horas_extras * 5  # 400% de regargo
    elif tipo_horas_extras == 6:
        return tarifa_hora * horas_extras * 6  # 500% de regargo
    else:
        return 0
#
#
#Calcula el salario bruto por medio de una suma.
def calcular_salario_bruto(salario_base, salario_hora_extra, bonificaciones, comisiones):
    return salario_base + salario_hora_extra + bonificaciones + comisiones
#
#
# Calcula las deducciones de ISSS, AFP y Renta.
def calcular_deducciones(salario_bruto):
    isss = salario_bruto * 0.03     # 3% de deduccion
    afp = salario_bruto * 0.0725    # 7.25% de deduccion
    #La deduccion de renta se calcula segun el total del salario bruto.
    if salario_bruto <= 487.60:
        renta = 0                                           #Si el sueldo es menor o igual a 487.60, no hay deduccion de renta.
    elif salario_bruto <= 642.85:
        renta = 17.48 + (0.1 * (salario_bruto - 487.60))      #Si el sueldo es mayor a 487.60 y menor o igual a 642.85, se aplica una tarifa fija de $17.48 más el 10% del exceso sobre $487.60.
    elif salario_bruto <= 915.81:
        renta = 32.70 + (0.2 * (salario_bruto - 642.85))      #Si el sueldo es mayor a 642.85 y menor o igual a 915.81, se aplica una tarifa fija de $32.70 más el 20% del exceso sobre $642.85.
    else:
        renta = 60.00 + (0.3 * (salario_bruto - 915.81))      #Si el sueldo es mayor a 915.81, se aplica una tarifa fija de $60.00 más el 30% del exceso sobre $915.81.
    deducciones_totales = isss + afp + renta
    return isss, afp, renta, deducciones_totales
#
#
# Calcula el salario neto por medio de una resta.
def calcular_salario_neto(salario_bruto, deducciones_totales):
    return salario_bruto - deducciones_totales
#
#
# Genera un archivo de texto con el recibo.
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
    print(f"◆ Recibo generado: {archivo_txt}")
#
#
# Funcion principal. Calcula el sueldo neto segun las entradas del usuario.
def calcular_salario():
    nombre = input("‣ Nombre del empleado: ") #nombre del empleado.
    salario_base = float(input("‣ Salario Base: ").strip()) #salario base.
    
    #Determina el tipo de horas extras.
    desea_horas_extras = (input("‣ ¿Desea ingresar horas extras? (si/no): ").strip().lower()) #pregunta si el usuario desea agregar horas extras.
    if desea_horas_extras == "si":
        
        #Menu para el tipo de horas extras.
        print("⦁ Tipos de Horas Extras:")     
        print("1. Diurnas")
        print("2. Nocturnas")
        print("3. Día de Descanso")
        print("4. Asueto")

        tipo_principal = int(input("‣ Seleccione el tipo de horas extras: ").strip()) #elige el tipo de horas extras.
        if tipo_principal == 1:
            tipo_horas_extras = 1
        elif tipo_principal == 2:
            tipo_horas_extras = 2
        elif tipo_principal == 3:
            #Menu para el tipo de horas extras en Día de Descanso.
            print("1. Diurnas\n2. Nocturnas")
            tipo_secundario = int(input("‣ Seleccione el tipo específico de horas extras en Día de Descanso: ").strip()) #elige el tipo de horas extras en Día de Descanso.
            if tipo_secundario == 1:
                tipo_horas_extras = 3
            elif tipo_secundario == 2:
                tipo_horas_extras = 4
            else:
                print("------------------------------------------------------------")
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                print("------------------------------------------------------------")
                return
        elif tipo_principal == 4:
            #Menu para el tipo de horas extras en Asueto.
            print("1. Diurnas\n2. Nocturnas")
            tipo_secundario = int(
                input("‣ Seleccione el tipo específico de horas extras en Asueto: ").strip()) #elige el tipo de horas extras en Asueto.
            if tipo_secundario == 1:
                tipo_horas_extras = 5
            elif tipo_secundario == 2:
                tipo_horas_extras = 6
            else:
                print("------------------------------------------------------------")
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                print("------------------------------------------------------------")
                return
        else:
            print("------------------------------------------------------------")
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            print("------------------------------------------------------------")
            return
        
        horas_extras = float(input("‣ Horas Extras: ").strip()) #horas extras.
    else:
        tipo_horas_extras = 0
        horas_extras = 0

    bonificaciones = float(input("‣ Bonificaciones: ").strip()) #bonificaciones.
    comisiones = float(input("‣ Comisiones: ").strip()) #comisiones.

    # Definición de funciones
    tarifa_hora = calcular_tarifa_hora(salario_base)
    
    salario_hora_extra = calcular_salario_hora_extra(tarifa_hora, tipo_horas_extras, horas_extras)
    
    salario_bruto = calcular_salario_bruto(salario_base, salario_hora_extra, bonificaciones, comisiones)

    isss, afp, renta, deducciones_totales = calcular_deducciones(salario_bruto)
    
    salario_neto = calcular_salario_neto(salario_bruto, deducciones_totales)
    
    #Datos en consola
    print("-----------------------------------------------------------")
    print("⦁ Información de Pago")                                       #Imprime el encabezado del recibo.
    print(f"⦁ Empleado: {nombre} ")                                    #Imprime el nombre del empleado.
    print(f"⦁ Salario Bruto:             ${salario_bruto:.2f}")          #Imprime el sueldo bruta.
    print(f"⦁ ISSS:                      ${isss:.2f}")                   #Imprime la deduccion de ISSS.
    print(f"⦁ AFP:                       ${afp:.2f}")                    #Imprime la deduccion de AFP.
    print(f"⦁ Renta:                     ${renta:.2f}")                  #Imprime la deduccion de renta.
    print(f"⦁ Deducciones Totales:       ${deducciones_totales:.2f}")    #Imprime las deducciones totales.
    print(f"⦁ Salario Neto:              ${salario_neto:.2f}")           #Imprime el sueldo neto.
    print("-----------------------------------------------------------")
    
    #Datos en archivo txt
    generar_recibo_txt(nombre, salario_bruto, isss, afp, renta, deducciones_totales, salario_neto)
#
#
# Programa principal. llama a la función Menu principal.
while True:
    mostrar_menu_principal()
    opcion = input("‣ Seleccione una opción: ").strip()
    if opcion == "1":
        calcular_salario()
    elif opcion == "2":
        print()
        print("Gracias por usar el sistema de nóminas. ¡Hasta luego!")
        print()
        break
    else:
        print()
        print("Opción no válida. Por favor, seleccione una opción del menú.")
        print()
