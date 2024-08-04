import sys
from pathlib import Path
from colorama import Fore, Style


def parse_file(path):
    try:
        for el in path.iterdir():
            el_name = el.parts[-1]
            shift = "  " * (len(el.parts) - 1)
            if el.is_dir():
                print(shift + Fore.BLUE + f"{el_name}" + '/' + Style.RESET_ALL)
                parse_file(el)
            else:
                print(shift + Fore.GREEN + f"{el_name}" + Style.RESET_ALL)
    except FileNotFoundError:
        print("Вказаний шлях не знайдено")
    except NotADirectoryError:
        print("Вказаний шлях не є директорією")


try:
    path = Path(sys.argv[1])
except IndexError:
    print("Невірна кількість аргументів")
    sys.exit()

parse_file(path)