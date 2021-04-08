number = float(input())

sign = ' '
value = 0

while sign != '=':
    i = input()
    i = i.split()
    sign = i[0]
    if len(i) > 1:
        value = float(i[1])
 
    if sign == '+':
        number += value
    elif sign == '-':
        number -= value
    elif sign == '*':
        number *= value
    elif sign == '/':
        number /= value
    elif sign == '**':
        number **= value

print(number)
