import os
import sys
import subprocess

# Определяем папку, где лежит сам исполняемый файл (.exe) или скрипт (.py)
if getattr(sys, 'frozen', False):
    folder = os.path.dirname(sys.executable)
else:
    folder = os.path.dirname(os.path.abspath(__file__))

target_extension = ".exe"

print(f"Рабочая папка: {folder}")

found = False

for file in os.listdir(folder):
    if file.lower().endswith(target_extension) and file != os.path.basename(sys.executable):
        found = True
        full_path = os.path.join(folder, file)
        print(f"Запускаю: {full_path}")
        try:
            subprocess.Popen([full_path], shell=True)
        except Exception as e:
            print(f"Ошибка при запуске {file}: {e}")

if not found:
    print(f"В папке нет файлов с расширением {target_extension}")
