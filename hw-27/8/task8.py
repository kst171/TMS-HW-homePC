import os
from statistics import median

def calculate_file_median(input_file):
    try:
        # Автоматическое определение папки, где лежит скрипт
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, input_file)

        # Чтение чисел из файла
        with open(file_path, "r", encoding="utf-8") as file:
            numbers = [float(line.strip()) for line in file if line.strip()]
            
        if not numbers:
            print("Файл пуст.")
            return

        # Вычисление медианы
        result = median(numbers)
        
        # Форматирование вывода (убираем .0 у целых чисел)
        final_result = int(result) if result.is_integer() else result
        
        print(f"Файл успешно прочитан: {input_file}")
        print(f"Всего элементов: {len(numbers)}")
        print("-" * 30)
        print(f"Медиана: {final_result}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
        print(f"Убедитесь, что он лежит в папке: {script_dir}")
    except ValueError:
        print("Ошибка: В файле содержатся не только числа.")

# Используем точное имя вашего файла со скриншота
file_name = "numbers_list.txt"
calculate_file_median(file_name)
