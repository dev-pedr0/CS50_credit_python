from cs50 import get_string

lenght = 0
second = False
sum = 0

while lenght <= 0:
    credit = get_string("Number: ")
    lenght = len(credit)

for i in range(lenght -1, -1, -1):
    number = ord(credit[i]) - ord('0')

    if second == True:
        number = number * 2

    while number != 0:
        sum = sum + (number % 10)
        number = number // 10

    second = not second

first_two = int(credit[0:2])

if (sum % 10) != 0:
    print("INVALID")
elif lenght == 15 and (first_two == 34 or first_two == 37):
    print("AMEX")
elif lenght == 16 and first_two > 50 and first_two < 56:
    print("MASTERCARD")
elif (lenght == 13 or lenght == 16) and credit[0] == '4':
    print("VISA")
else:
    print("INVALID")
