import string

def count_char_types(input_string):
    # Инициализация счетчиков
    upper_case = 0
    lower_case = 0
    digits = 0
    punctuation = 0
    others = 0 # Для пробелов и спецсимволов, не входящих в пунктуацию

    # Перебор каждого символа в строке
    for char in input_string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        elif char.isdigit():
            digits += 1
        elif char in string.punctuation:
            punctuation += 1
        else:
            others += 1

    # Вывод результатов
    print(f"Строка: '{input_string}'")
    print("-" * 20)
    print(f"Букв в верхнем регистре: {upper_case}")
    print(f"Букв в нижнем регистре: {lower_case}")
    print(f"Цифр: {digits}")
    print(f"Знаков пунктуации: {punctuation}")
    print(f"Остальных символов (пробелы и т.д.): {others}")

# Пример использования:
text = input("Введите строку: ")
count_char_types(text)
