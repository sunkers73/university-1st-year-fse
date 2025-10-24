# Вывод прямоугольника
def rectangle(height, width, symbol):
    print(f"Прямоугольник {height}*{width}:")
    for i in range(height):
        for j in range(width):
            print(symbol, end="")
        print()

# Вывод треугольника
def triangle(size, symbol):
    print("Правильный треугольник:")
    for i in range(size):
            for j in range(i+1):
                print(symbol, end='')
            print()

# Вывод рамки
def frame(height, width, symbol):
    print(f"Рамка {height}*{width}:")
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print(symbol, end='')
            else:
                print(' ', end='')
        print()

# Ввод данных
figure = input("Введите фигуру (прямоугольник(п), треугольник(т), рамка(р)): ")
symbol = input("Введите символ из которого будет состоять фигура: ")

if figure == "прямоугольник" or figure == "п":
    rectangle(int(input("Введите высоту: ")), int(input("Введите ширину: ")), symbol)
elif figure == "треугольник" or figure == "т":
    triangle(int(input("Введите размер правильного треугольника: ")), symbol)
elif figure == "рамка" or figure == "р":
    frame(int(input("Введите высоту: ")), int(input("Введите ширину: ")), symbol)
