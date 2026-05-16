import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # Метод площади: S = π * r²
    def get_area(self):
        return math.pi * (self.radius ** 2)

    # Метод длины окружности: C = 2 * π * r
    def get_circumference(self):
        return 2 * math.pi * self.radius


# Создаем список объектов (экземпляров класса)
circles_list = [
    Circle(3, "Красный"),
    Circle(15, "Синий"),
    Circle(4.8, "Зеленый"),
    Circle(35, "Желтый")
]

for index, circle in enumerate(circles_list, 1):
    # Вычисляем значения и округляем до 2 знаков после запятой
    area = round(circle.get_area(), 2)
    circumference = round(circle.get_circumference(), 2)
    
    # Выводим информацию о текущем круге
    print(f"Круг №{index} | Цвет: {circle.color} | Радиус: {circle.radius}")
    print(f"  -> Площадь: {area}")
    print(f"  -> Длина окружности: {circumference}")
    print("-" * 40)
