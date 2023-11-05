import os
import sys
import time
import logging

import colorama
from colorama import Fore, Back
from art import tprint

from app.directory_clean import delete_files_in_folder, delete_everything_in_folder
from app.files_rename import increment_rename, random_rename

colorama.init(autoreset=True)


def main_menu():
    os.system('cls')
    print(Back.BLUE + Fore.BLACK + "FileManager!")
    print(Fore.GREEN + "Выберите необходимую опцию!")
    while True:
        print("1. Очистка указанной директории")
        print("2. Переименовывание файлов")
        print("3. Резервная копия директории " + Fore.RED + "ВРЕМЕННО НЕ РАБОТАЕТ!")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")

        if cmd == "1":
            directory_clean_menu()
        elif cmd == "2":
            rename_menu()
        elif cmd == "3":
            pass
        elif cmd == "0":
            sys.exit()
        else:
            print(Fore.RED + "Вы ввели неправильное значение")


def directory_clean_menu():
    os.system('cls')
    print(Fore.GREEN + "Вы выбрали очистку директории")
    while True:
        print("1. Удаление файлов")
        print("2. Удаление файлов и поддерикторий")
        print("0. Выйти в главное меню")
        cmd = input("Выберите пункт: ")

        if cmd == "1":
            folder_path = input("Введите путь: ")
            delete_files_in_folder(folder_path)
            print(Fore.GREEN + "Удаление завершено успешо!")
            print(Fore.BLUE + "Возвращаю Вас в главное меню!")
            main_menu()
            break
        elif cmd == "2":
            folder_path = input("Введите путь: ")
            delete_everything_in_folder(folder_path)
            print(Fore.GREEN + "Удаление завершено успешо!")
            print(Fore.BLUE + "Возвращаю Вас в главное меню!")
            main_menu()
            break
        elif cmd == "0":
            main_menu()
            break
        else:
            print(Fore.RED + "Вы ввели неправильное значение")


def rename_menu():
    os.system('cls')
    print(Fore.GREEN + "Вы выбрали переименовывание файлов")
    while True:
        print("1. По порядку")
        print("2. Случайно")
        print("0. Выйти в главное меню")
        cmd = input("Выберите пункт: ")

        if cmd == "1":
            folder_path = input("Введите путь: ")
            increment_rename(folder_path)
            print(Fore.GREEN + "Переименовывание завершено успешо!")
            print(Fore.BLUE + "Возвращаю Вас в главное меню!")
            main_menu()
            break
        elif cmd == "2":
            folder_path = input("Введите путь: ")
            random_rename(folder_path)
            print(Fore.GREEN + "Переименовывание завершено успешо!")
            print(Fore.BLUE + "Возвращаю Вас в главное меню!")
            main_menu()
            break
        elif cmd == "0":
            main_menu()
            break
        else:
            print(Fore.RED + "Вы ввели неправильное значение")


if __name__ == '__main__':
    logging.info("An INFO")
    os.system('cls')
    tprint("FileManager")
    time.sleep(1)
    main_menu()
