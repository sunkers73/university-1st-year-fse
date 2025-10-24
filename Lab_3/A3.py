# Ввод данных

previous_value = int(input("Введите предыдущее показание счётчика: "))
current_value = int(input("Введите текущее показание счётчика: "))

# Вычисление использованного объёма газа
if current_value >= previous_value:
    gas_used = current_value - previous_value
else:
    gas_used = (10000 - previous_value) + current_value

# Вычисление суммы к оплате
if gas_used <= 300:
    price = 21
elif gas_used <= 600:
    price = 21 + (gas_used - 300) * 0.06
elif gas_used <= 800:
    price = 21 + (300 * 0.06) + (gas_used - 600) * 0.04
else:
    price = 21 + (300 * 0.06) + (200 * 0.04) + (gas_used - 800) * 0.025

# Вычисление средней цены за кубометр
average_price = price / gas_used

# Вывод результатов
print(f"Предыдущее показание счётчика: {previous_value} кубометров")
print(f"Текущее показание счётчика: {current_value} кубометров")
print(f"Объём использованного газа: {gas_used} кубометров")
print(f"Сумма к оплате: {price:.2f} $")
print(f"Средняя цена за кубометр: {average_price:.2f} $/m^3")
