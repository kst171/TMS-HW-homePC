import os

# Укажите здесь путь к любой нужной папке (буква r перед кавычками обязательна!)
folder_path = r"H:\learning\TMS_DevOps\HW\hw-28\mydir"

# Получаем список файлов
for file in os.listdir(folder_path):
    print(file)