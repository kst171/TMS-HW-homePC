def read_list_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # Читаем строки, удаляем пробелы/переносы и фильтруем пустые строки
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return None

def main():
    # Пути к файлам
    file1_path = "H:\learning\TMS_DevOps\HW\hw-27\list1.txt"
    file2_path = "H:\learning\TMS_DevOps\HW\hw-27\list2.txt"

    # Чтение данных
    list1 = read_list_from_file(file1_path)
    list2 = read_list_from_file(file2_path)

    # Если оба файла успешно прочитаны
    if list1 is not None and list2 is not None:
        # Находим пересечение через множества
        common = set(list1) & set(list2)
        
        print(f"Элементов в первом файле: {len(list1)}")
        print(f"Элементов во втором файле: {len(list2)}")
        print("-" * 30)
        print(f"Общие элементы ({len(common)} шт.):")
        
        for item in sorted(common):
            print(f"- {item}")

if __name__ == "__main__":
    main()
