def isValidNumber(number):
    return number.isdigit() and len(number) in [13, 15, 16]

def getCheckSum(number):
    checkSum = 0
    number = number[::-1] # переворот строки
    for i in range(len(number)):
        digit = int(number[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checkSum += digit
    return checkSum

def getCardType(number):
    if (len(number) in [13, 16]) and number[0] == "4":
        return "Visa"
    if len(number) == 15 and (number[:2] == "34" or number[:2] == "37"):
        return "American Express"
    if len(number) == 16 and number[:2] in ["51", "52", "53", "54", "55"]:
        return "Master Card"
    return "Invalid"

cardNumber = input("Введите номер банковской карты: ")

if isValidNumber(cardNumber):
    if getCheckSum(cardNumber) % 10 == 0:
        print(getCardType(cardNumber))
    else:
        print("Invalid")
else:
    print("Invalid")