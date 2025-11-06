import re

def split_sentences(text):
    sentences = re.split(r'(?<=[.?!])\s+', text.strip())

    return sentences


text = input("Введите исходный текст: ")

sentences = split_sentences(text)
for s in sentences:
    print(s)
print("Количество предложений:", len(sentences))