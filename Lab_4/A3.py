# Ввод данных c проверкой корректности
packets = input("Введите последовательность пакетов: ")
while len(packets) < 5 or not all(char in '01' for char in packets):
    print("Ошибка ввода(необходимо не менее пяти символов и использовать только 0 и 1)")
    packets = input("Введите последовательность пакетов: ")

# Вычисления результатов
total_quantity_packets = len(packets)

quantity_lost_packets = packets.count('0')

max_zeros = 0
current_zeros = 0
for packet in packets:
    if packet == "0":
        current_zeros += 1
        if current_zeros > max_zeros:
            max_zeros = current_zeros
    else:
        current_zeros = 0

packet_loss_percentage = quantity_lost_packets / total_quantity_packets * 100

if packet_loss_percentage < 1:
    connection_quality = "Отличное качество"
elif packet_loss_percentage < 5:
    connection_quality = "Хорошее качество"
elif packet_loss_percentage < 10:
    connection_quality = "Удовлетворительное качество"
elif packet_loss_percentage < 20:
    connection_quality = "Плохое качество"
else:
    connection_quality = "Критическое состояние сети"

# Вывод результатов
print("Общее кол-во пакетов:", total_quantity_packets)
print("Кол-во потерянных пакетов:", quantity_lost_packets)
print(f"Процент потерь: {packet_loss_percentage:.2f} %")
print("Длина самой длинной последовательности потерянных пакетов: ", max_zeros)
print("Качество связи: ", connection_quality)