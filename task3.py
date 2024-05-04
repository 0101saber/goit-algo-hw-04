import sys
from pathlib import Path
from colorama import Fore, Back, Style


def print_file_name(directory):
    for path in directory.iterdir():
        if path.is_dir():
            print('-' * (len(path.parts) - 1), f"{Fore.BLUE} {path.name} {Fore.RESET}")
            print_file_name(path)
        if path.is_file():
            print('-' * len(path.parts), f"{Fore.YELLOW} {path.name} {Fore.RESET}")


def main():
    if len(sys.argv) > 1:
        path_input = sys.argv[1]
        directory = Path(path_input)
        if directory.exists() and directory.is_dir():
            print_file_name(directory)
        else:
            print(f"Шляху '{path_input}' не існує або не є директорією")


if __name__ == "__main__":
    main()
