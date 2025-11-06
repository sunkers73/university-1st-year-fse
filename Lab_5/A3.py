def abbreviation(text):
    words = text.split()
    abbrev = ''

    for w in words:
        if len(w) >= 3:
            abbrev += w[0].upper()

    return abbrev


text = input("Введите исходный текст: ")
print(abbreviation(text))