import os
import subprocess

# Папка, где лежит сам скрипт
folder = os.path.dirname(os.path.abspath(__file__))

# Формат, который нужно запустить
target_extension = ".exe"  # можно заменить, например, на ".mp3", ".txt" и т.д.

# Проходим по всем файлам в папке
for file in os.listdir(folder):
    if file.lower().endswith(target_extension):
        full_path = os.path.join(folder, file)
        print(f"Запускаю: {file}")
        try:
            # subprocess позволяет запускать любой файл
            subprocess.Popen(full_path, shell=True)
        except Exception as e:
            print(f"Ошибка при запуске {file}: {e}")
