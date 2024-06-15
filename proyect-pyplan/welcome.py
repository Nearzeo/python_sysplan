# welcome.py
from utils import RESET_COLOR, BRIGHT, BLUE

def imprimir_bienvenida():
    bienvenido = [
        f"{BLUE}{BRIGHT} ____  _                                  _     _       ",
        f"{BLUE}{BRIGHT}| __ )|_|  ___  _ __ __    __ ___  _ __  |_| __| | ___  ",
        f"{BLUE}{BRIGHT}|  _ \\ _ / __ \\| '_ \\\\ \\  / / __ \\| '_ \\  _ / _` |/ _ \\ ",
        f"{BLUE}{BRIGHT}| |_) | ||  __/| | | |\\ \\/ /|  __/| | | || | (_| | (_) |",
        f"{BLUE}{BRIGHT}|____/|_| \\___||_| |_| \\__/  \\___||_| |_||_|\\__,_|\\___/ {RESET_COLOR}",
    ]
    al = [
        f"{BLUE}{BRIGHT}    _     _ ",
        f"{BLUE}{BRIGHT}   / \\   | |",
        f"{BLUE}{BRIGHT}  / _ \\  | |",
        f"{BLUE}{BRIGHT} / ___ \\ | |",
        f"{BLUE}{BRIGHT}/_/   \\_\\|_|{RESET_COLOR}",
    ]
    sistema = [
        f"{BLUE}{BRIGHT}  ____  _                           ",
        f"{BLUE}{BRIGHT} / ___||_| ___ _____  ___   _ ___ __   __ _ ",
        f"{BLUE}{BRIGHT} \\___ \\ _ / __|_   _|/ __ \\| '_  '_ \\ / _ '|",
        f"{BLUE}{BRIGHT}  ___) | |\\__ \\ | | |   __/| | | | | | (_  |",
        f"{BLUE}{BRIGHT} |____/|_||___/ |_|  \\____||_| |_| |_\\__,_|{RESET_COLOR}",
    ]

    for line in bienvenido:
        print(line)
    for line in al:
        print(line)
    for line in sistema:
        print(line)
