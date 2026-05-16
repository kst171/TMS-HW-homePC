def multiply_numbers(a, b):
    return a * b

try:
    # Запрос чисел у пользователя
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # Вызов функции и сохранение результата
    result = multiply_numbers(num1, num2)

    # Вывод
    print(f"Результат умножения: {result}")

except ValueError:
    print("Ошибка: Пожалуйста, вводите только числа.")