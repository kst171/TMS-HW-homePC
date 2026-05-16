def sort_and_save_numbers(input_file, output_file):
    try:
        # 1. Чтение чисел из исходного файла
        with open(input_file, "r", encoding="utf-8") as file:
            numbers = [int(line.strip()) for line in file if line.strip()]
            
        if not numbers:
            print("Исходный файл пуст.")
            return

        # 2. Сортировка по убыванию
        numbers.sort(reverse=True)
        
        # 3. Запись результата в новый файл
        with open(output_file, "w", encoding="utf-8") as file:
            for num in numbers:
                file.write(f"{num}\n")
        
        # 4. Вывод отчета в консоль
        print(f"Успешно обработано чисел: {len(numbers)}")
        print(f"Результат сохранен в файл: {output_file}")
        
    except FileNotFoundError:
        print(f"Ошибка: Исходный файл '{input_file}' не найден.")
    except ValueError:
        print("Ошибка: В файле обнаружены некорректные данные (не числа).")

# Настройки имен файлов
input_name = "numbers_list.txt"
output_name = "sorted_numbers.txt"

# Запуск функции
sort_and_save_numbers(input_name, output_name)
