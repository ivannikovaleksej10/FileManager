import shutil
import os


# Удаление файлов в папке
def delete_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    print(f'В указанной папке {len(files)} файлов!')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')


# Удаление файлов и поддерикторий в папке
def delete_everything_in_folder(folder_path):
    files = os.listdir(folder_path)
    print(f'В указанной папке {len(files)} файлов!')
    shutil.rmtree(folder_path)
    os.mkdir(folder_path)
