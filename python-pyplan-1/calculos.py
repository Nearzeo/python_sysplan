def calcular_tarifa_hora(salario_base):
    return salario_base / 22 / 8

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

def calcular_salario_bruto(salario_base, salario_hora_extra, bonificaciones, comisiones):
    return salario_base + salario_hora_extra + bonificaciones + comisiones

def calcular_deducciones(salario_bruto):
    isss = salario_bruto * 0.03     # 3% de deduccion
    afp = salario_bruto * 0.0725    # 7.25% de deduccion
    if salario_bruto <= 487.60:
        renta = 0
    elif salario_bruto <= 642.85:
        renta = 17.48 + (0.1 * (salario_bruto - 487.60))
    elif salario_bruto <= 915.81:
        renta = 32.70 + (0.2 * (salario_bruto - 642.85))
    else:
        renta = 60.00 + (0.3 * (salario_bruto - 915.81))
    deducciones_totales = isss + afp + renta
    return isss, afp, renta, deducciones_totales

def calcular_salario_neto(salario_bruto, deducciones_totales):
    return salario_bruto - deducciones_totales