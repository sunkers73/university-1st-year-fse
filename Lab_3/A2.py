password = input("Введите пароль: ") # ввод данных

errors = []  # список ошибок
special_characters = "*-#"  # допустимые спецсимволы

# Проверяем длину
if len(password) != 8:
    errors.append("Длина пароля не равна 8")

# Проверка наличия хотя бы одной заглавной буквы
if not any(symbol.isupper() for symbol in password):
    errors.append("В пароле отсутствуют заглавные буквы")

# Проверка наличия хотя бы одной строчной буквы
if not any(symbol.islower() for symbol in password):
    errors.append("В пароле отсутствуют строчные буквы")

# Проверка наличия хотя бы одной цифры
if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")

# Проверка наличия хотя бы одного спецсимвола (*, -, #)
if not any(symbol in special_characters for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")

# Проверка отсутствия непредусмотренных символов
if not all(symbol.isalnum() or symbol in special_characters for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")

# Вывод результата
if len(errors) == 0:
    print("Надёжный пароль")
else:
    print("Ошибки: ")
    for elements in errors:
        print("-", elements)
