# welcome.py
from utils import RESET_COLOR, BRIGHT, CYAN, MAGENTA

def imprimir_bienvenida():
    bienvenido = [
    f"{MAGENTA}{BRIGHT}  ____  _                                  _     _       ",
    f"{MAGENTA}{BRIGHT} | __ )|_|  ___  _ __ __    __ ___  _ __  |_| __| | ___  ",
    f"{MAGENTA}{BRIGHT} |  _ \ _ / __ \| '_ \\ \  / / __ \| '_ \  _ / _` |/ _ \ ",
    f"{MAGENTA}{BRIGHT} | |_) | ||  __/| | | |\ \/ /|  __/| | | || | (_| | (_) |",
    f"{MAGENTA}{BRIGHT} |____/|_| \___||_| |_| \__/  \___||_| |_||_|\__,_|\___/ {RESET_COLOR}",
    ]

    al = [
    f"{CYAN}{BRIGHT}     _     _ ",
    f"{CYAN}{BRIGHT}    / \   | |",
    f"{CYAN}{BRIGHT}   / _ \  | |",
    f"{CYAN}{BRIGHT}  / ___ \ | |",
    f"{CYAN}{BRIGHT} /_/   \_\|_|{RESET_COLOR}",
    ]

    sistema = [
    f"{MAGENTA}{BRIGHT}  ____  _                           ",
    f"{MAGENTA}{BRIGHT} / ___||_| ___ _____  ___   _ ___ __   __ _ ",
    f"{MAGENTA}{BRIGHT} \___ \ _ / __|_   _|/ __ \| '_  '_ \ / _ '|",
    f"{MAGENTA}{BRIGHT}  ___) | |\__ \ | | |   __/| | | | | | (_  |",
    f"{MAGENTA}{BRIGHT} |____/|_||___/ |_|  \____||_| |_| |_|\__,_|{RESET_COLOR}",
    ]

    for line in bienvenido:
        print(line)
    for line in al:
        print(line)
    for line in sistema:
        print(line)
