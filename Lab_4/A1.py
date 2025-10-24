# Импорт модулей
import random
import time

# Ввод данных
N = int(input("Введите кол-во примеров: "))

#Объявление переменных
current_example = 1
num_of_correct_ans = 0
total_time = 0

# Цикл для генерации и проверки N примеров
for i in range(N):
    num1, num2 = random.randint(2, 9), random.randint(2, 9)

    print(f"Текущий пример {current_example}/{N}")
    current_example += 1

    time_start = time.time()
    while True:
        try:
            answer = int(input(f"{num1} * {num2} = "))
            break
        except ValueError:
            print("Ошибка, введите целое число!")
    time_end = time.time()

    total_time += time_end - time_start

    if answer == num1 * num2:
        num_of_correct_ans += 1
        print(f"Верно! (Время: {time_end - time_start:.2f} сек)")
    else:
        print(f"Неверно! (Время: {time_end - time_start:.2f} сек)")

# Вывод результатов
print("")
print("Статистика:")
print(f"Общее время: {total_time:.2f} cек")
print(f"Среднее время на вопрос: {total_time/N:.2f} сек")
print(f"Правильных ответов: {num_of_correct_ans}/{N}")
print(f"Процент правильных: {num_of_correct_ans/N*100:.1f}%")
