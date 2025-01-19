import os

from Felhasznaloi_interfesz.menu import UI


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')





if __name__ == '__main__':
    menu = UI()
    menu.adat_init()
    menu.start()

    while True:
        menu.bemenet_keres()
