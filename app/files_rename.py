import os
import random
import string


def increment_rename(folder_path):
    files = os.listdir(folder_path)
    print(f'В указанной папке {len(files)} файлов!')

    i = 1

    for file_name in os.listdir(folder_path):
        base_name, ext = os.path.splitext(file_name)

        if ext.lower() not in ['.jpg', '.jpeg', '.webp', '.png', '.gif', '.pdf', '.bmp', '.raw', '.tiff']:
            continue

        abs_file_name = os.path.join(folder_path, file_name)

        new_abs_file_name = os.path.join(folder_path, str(i) + ext)
        try:
            os.rename(abs_file_name, new_abs_file_name)
        except Exception as e:
            print(f'Ошибка при переименовывание файла {abs_file_name}. {e}')

        i += 1


def random_rename(folder_path):
    files = os.listdir(folder_path)
    print(f'В указанной папке {len(files)} файлов!')

    letters = string.ascii_lowercase

    for file_name in os.listdir(folder_path):
        base_name, ext = os.path.splitext(file_name)

        if ext.lower() not in ['.jpg', '.jpeg', '.webp', '.png', '.gif', '.pdf', '.bmp', '.raw', '.tiff']:
            continue

        abs_file_name = os.path.join(folder_path, file_name)

        rand_string = ''.join(random.choice(letters) for i in range(8))

        new_abs_file_name = os.path.join(folder_path, str(rand_string) + ext)
        try:
            os.rename(abs_file_name, new_abs_file_name)
        except Exception as e:
            print(f'Ошибка при переименовывание файла {abs_file_name}. {e}')

