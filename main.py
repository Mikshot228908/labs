'''
num = int(input("Введите натуральное число,которое меньше 1_000_000_000:"))
if num > 1000000000:
    print("Input error!!!!")
else:
    print("Самая большая цифра введёного числа:",max(str(num)))



num = input("Введите натуральное число, которое меньше 1_000_000_000: ")

if not num.isdigit() or int(num) >= 1_000_000_000:
    print("Input error!!!!")
else:
    print("Самая большая цифра введённого числа:", max(num))
'''

