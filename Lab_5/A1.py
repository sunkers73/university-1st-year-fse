def shortening_text(text):
    result = ''
    inside = 0

    for char in text:
        if char == '(':
            inside += 1
        elif char == ')':
            if inside > 0:
                inside -= 1
        elif inside == 0:
            result += char

    return result


text = input("Введите исходный текст: ")
print(shortening_text(text))