import datetime
from welcome import imprimir_bienvenida  # Importa la función desde welcome.py

# Diccionario para almacenar los empleados
empleados = {}

# Muestra el menu principal del sistema.
def mostrar_menu_principal():
    print("\n-----------------------------------------------------------")
    print("Bienvenido al Sistema de Planillas")
    print("-----------------------------------------------------------")
    print("⦁ Menú Principal:")
    print("1. Ingresar Empleado a la Planilla")
    print("2. Calcular Salario")
    print("3. Eliminar Empleado de la Planilla")
    print("4. Ver Lista de Empleados")
    print("5. Salir")

# Calcula la tarifa por hora, suponiendo que se trabaje 22 dias al mes y 8 horas por semana.
def calcular_tarifa_hora(salario_base):
    return salario_base / 22 / 8

# Calcula el salario por hora extra. Varia segun el tipo de horas extras
def calcular_salario_hora_extra(tarifa_hora, tipo_horas_extras, horas_extras):
    if tipo_horas_extras == 1:
        return tarifa_hora * horas_extras * 2  # 100% de recargo
    elif tipo_horas_extras == 2:
        return tarifa_hora * horas_extras * 2.5  # 150% de recargo
    elif tipo_horas_extras == 3:
        return tarifa_hora * horas_extras * 4  # 300% de recargo
    elif tipo_horas_extras == 4:
        return tarifa_hora * horas_extras * 4.75  # 375% de recargo
    elif tipo_horas_extras == 5:
        return tarifa_hora * horas_extras * 5  # 400% de recargo
    elif tipo_horas_extras == 6:
        return tarifa_hora * horas_extras * 6  # 500% de recargo
    else:
        return 0

# Calcula el salario bruto por medio de una suma.
def calcular_salario_bruto(salario_base, salario_hora_extra, bonificaciones, comisiones):
    return salario_base + salario_hora_extra + bonificaciones + comisiones

# Calcula las deducciones de ISSS, AFP y Renta.
def calcular_deducciones(salario_bruto):
    isss = salario_bruto * 0.03     # 3% de deduccion
    afp = salario_bruto * 0.0725    # 7.25% de deduccion
    
    #La deduccion de renta se calcula segun el total del salario bruto.
    if salario_bruto <= 487.60:
        renta = 0                                           #Si el sueldo es menor o igual a 487.60, no hay deduccion de renta.
    elif salario_bruto <= 642.85:
        renta = 17.48 + (0.1 * (salario_bruto - 487.60))    #Si el sueldo es mayor a 487.60 y menor o igual a 642.85, se aplica una tarifa fija de $17.48 más el 10% del exceso sobre $487.60.
    elif salario_bruto <= 915.81:
        renta = 32.70 + (0.2 * (salario_bruto - 642.85))    #Si el sueldo es mayor a 642.85 y menor o igual a 915.81, se aplica una tarifa fija de $32.70 más el 20% del exceso sobre $642.85.
    else:
        renta = 60.00 + (0.3 * (salario_bruto - 915.81))    #Si el sueldo es mayor a 915.81, se aplica una tarifa fija de $60.00 más el 30% del exceso sobre $915.81.
    deducciones_totales = isss + afp + renta
    return isss, afp, renta, deducciones_totales

# Calcula el salario neto por medio de una resta.
def calcular_salario_neto(salario_bruto, deducciones_totales):
    return salario_bruto - deducciones_totales

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

# Agrega un nuevo empleado al diccionario
def ingresar_empleado():
    print("-----------------------------------------------------------")
    print("Ingrese los datos del nuevo empleado:")
    print("-----------------------------------------------------------")
    nombre = input("‣ Nombre del empleado: ").strip()
    if nombre in empleados:
        print("El empleado ya existe en la planilla.")
        return

    puesto = input("‣ Puesto de trabajo: ").strip()
    sexo = input("‣ Sexo (m/f): ").strip()
    edad = int(input("‣ Edad: ").strip())
    telefono = input("‣ Teléfono: ").strip()
    correo = input("‣ Correo electrónico: ").strip()
    salario_base = float(input("‣ Salario Base: ").strip())
    print("-----------------------------------------------------------")

    empleados[nombre] = {
        'puesto': puesto,
        'sexo': sexo,
        'edad': edad,
        'telefono': telefono,
        'correo': correo,
        'salario_base': salario_base
    }

    print(f"Empleado {nombre} ha sido agregado a la planilla.")

# Calcula el sueldo neto segun las entradas del usuario.
def calcular_salario():
    print("-----------------------------------------------------------")
    print("‣ Ingrese los siguientes datos: \n(Recuerde que el sistema esta diseñado para calcular el sueldo neto mesual.)")
    print("-----------------------------------------------------------")
    nombre = input("‣ Nombre del empleado: ").strip()
    if nombre not in empleados:
        print("-----------------------------------------------------------")
        print("El empleado no existe en la planilla.")
        return

    empleado = empleados[nombre]
    salario_base = empleado['salario_base']

    desea_horas_extras = (input("‣ ¿Desea ingresar horas extras? (si/no): ").strip().lower()) #pregunta si el usuario desea agregar horas extras.
    if desea_horas_extras == "si":
        
        #Menu para el tipo de horas extras.
        print("-----------------------------------------------------------")
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
            print("-----------------------------------------------------------")
            print("1. Diurnas\n2. Nocturnas")
            tipo_secundario = int(input("‣ Seleccione el tipo específico de horas extras en Día de Descanso: ").strip()) #elige el tipo de horas extras en Día de Descanso.
            if tipo_secundario == 1:
                tipo_horas_extras = 3
            elif tipo_secundario == 2:
                tipo_horas_extras = 4
            else:
                print("-----------------------------------------------------------")
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                print("-----------------------------------------------------------")
                return
        elif tipo_principal == 4:
            #Menu para el tipo de horas extras en Asueto.
            print("1. Diurnas\n2. Nocturnas")
            tipo_secundario = int(input("‣ Seleccione el tipo específico de horas extras en Asueto: ").strip()) #elige el tipo de horas extras en Asueto.
            if tipo_secundario == 1:
                tipo_horas_extras = 5
            elif tipo_secundario == 2:
                tipo_horas_extras = 6
            else:
                print("-------------------------------------------------------------------------------------")
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                print("-------------------------------------------------------------------------------------")
                return
        else:
            print("-------------------------------------------------------------------------------------")
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            print("-------------------------------------------------------------------------------------")
            return
        
        horas_extras = float(input("‣ Horas Extras Trabajadas: ").strip()) #horas extras.
    else:
        tipo_horas_extras = 0
        horas_extras = 0

    bonificaciones = float(input("‣ Bonificaciones: ").strip()) #bonificaciones.
    comisiones = float(input("‣ Comisiones: ").strip()) #comisiones.

    tarifa_hora = calcular_tarifa_hora(salario_base)
    salario_hora_extra = calcular_salario_hora_extra(tarifa_hora, tipo_horas_extras, horas_extras)
    salario_bruto = calcular_salario_bruto(salario_base, salario_hora_extra, bonificaciones, comisiones)
    isss, afp, renta, deducciones_totales = calcular_deducciones(salario_bruto)
    salario_neto = calcular_salario_neto(salario_bruto, deducciones_totales)

    print("------------------------------------------------------------------------------------")
    print("⦁ Información de Pago")                                       #Imprime el encabezado del recibo.
    print(f"⦁ Empleado: {nombre} ")                                    #Imprime el nombre del empleado.
    print(f"⦁ Salario Bruto:             ${salario_bruto:.2f}")          #Imprime el sueldo bruto.
    print(f"⦁ ISSS:                      ${isss:.2f}")                   #Imprime la deduccion de ISSS.
    print(f"⦁ AFP:                       ${afp:.2f}")                    #Imprime la deduccion de AFP.
    print(f"⦁ Renta:                     ${renta:.2f}")                  #Imprime la deduccion de renta.
    print(f"⦁ Deducciones Totales:       ${deducciones_totales:.2f}")    #Imprime las deducciones totales.
    print(f"⦁ Salario Neto:              ${salario_neto:.2f}")           #Imprime el sueldo neto.
    print("------------------------------------------------------------------------------------")
    
    desea_generar_recibo = (input("‣ ¿Desea generar un archivo de recibo? (si/no): ").strip().lower())
    if desea_generar_recibo == "si":
        generar_recibo_txt(nombre, salario_bruto, isss, afp, renta, deducciones_totales, salario_neto)

# Elimina un empleado del diccionario
def eliminar_empleado():
    print("-----------------------------------------------------------")
    print("⦁ Ingrese el nombre del empleado a eliminar:")
    print("-----------------------------------------------------------")
    nombre = input("‣ Nombre del empleado a eliminar: ").strip()
    if nombre not in empleados:
        print("-----------------------------------------------------------")
        print("El empleado no existe en la planilla.")
        return

    confirmacion = input(f"¿Está seguro que desea eliminar a {nombre} de la planilla? (si/no): ").strip().lower()
    if confirmacion == "si":
        del empleados[nombre]
        print(f"Empleado {nombre} ha sido eliminado de la planilla.")
    else:
        print("-----------------------------------------------------------")
        print("Operación cancelada.")

# Muestra la lista de empleados y su información
def ver_lista_empleados():
    if not empleados:
        print("-----------------------------------------------------------")
        print("No hay empleados en la planilla.")
        return

    print("-----------------------------------------------------------")
    print("⦁ Lista de Empleados:")
    print("-----------------------------------------------------------")
    for nombre, info in empleados.items():
        print(f"\nEmpleado: {nombre}")
        print(f"  Puesto: {info['puesto']}")
        print(f"  Sexo: {info['sexo']}")
        print(f"  Edad: {info['edad']}")
        print(f"  Teléfono: {info['telefono']}")
        print(f"  Correo: {info['correo']}")
        print(f"  Salario Base: ${info['salario_base']:.2f}")

# Programa principal. llama a la función Menu principal.
if __name__ == "__main__":
    imprimir_bienvenida()  # Llama a la función para imprimir la bienvenida
    while True:
        mostrar_menu_principal()
        opcion = input("‣ Seleccione una opción: ").strip()
        if opcion == "1":
            ingresar_empleado()
        elif opcion == "2":
            calcular_salario()
        elif opcion == "3":
            eliminar_empleado()
        elif opcion == "4":
            ver_lista_empleados()
        elif opcion == "5":
            print("-----------------------------------------------------------")
            print("Gracias por usar el sistema de nóminas. ¡Hasta luego!")
            print("-----------------------------------------------------------")
            break
        else:
            print("-----------------------------------------------------------")
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            
