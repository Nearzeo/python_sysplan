# Código de color morado usando ANSI
purple = '\033[38;2;192;189;242m'
reset_color = '\033[0m'
bright = '\033[1m'

# Patrones ASCII para "Bienvenido", "al", y "Sistema"
bienvenido = [
    r" ____  _                                  _     _       ",
    r"| __ )|_|  ___  _ __ __    __ ___  _ __  |_| __| | ___  ",
    r"|  _ \ _ / __ \| '_ \\ \  / / __ \| '_ \  _ / _` |/ _ \ ",
    r"| |_) | ||  __/| | | |\ \/ /|  __/| | | || | (_| | (_) |",
    r"|____/|_| \___||_| |_| \__/  \___||_| |_||_|\__,_|\___/ ",
]

al = [
    r"    _     _ ",
    r"   / \   | |",
    r"  / _ \  | |",
    r" / ___ \ | |",
    r"/_/   \_\|_|",
]

sistema = [
    r"  ____  _                           ",
    r" / ___||_| ___ _____  ___   _ ___ __   __ _ ",
    r" \___ \ _ / __|_   _|/ __ \| '_  '_ \ / _ '|",
    r"  ___) | |\__ \ | | |   __/| | | | | | (_  |",
    r" |____/|_||___/ |_|  \____||_| |_| |_|\__,_|",
]

def imprimir_bienvenida():
    # Imprimir los patrones con color morado y estilo brillante
    print(purple + bright)
    for line in bienvenido:
        print(line)
    for line in al:
        print(line)
    for line in sistema:
        print(line)
    print(reset_color)
