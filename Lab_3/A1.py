# Ввод данных
x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))

# Определение четвертей
def quarter_check(x, y):
    if x > 0 and y > 0:
        return "I"
    if x < 0 and y > 0:
        return "II"
    if x < 0 and y < 0:
        return "III"
    if x > 0 and y < 0:
        return "IV"

quarter1 = quarter_check(x1, y1)
quarter2 = quarter_check(x2, y2)

# Вывод результата
if quarter1 == quarter2:
    print("Yes,", quarter1)
else:
    print("No")