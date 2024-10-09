num_a = int(input("Введите число a:"))
num_b = int(input("Введите число b:"))

if num_a>num_b:
    num_a,num_b = num_b,num_a


print("Положительные числа в диапазоне от num_a до num_b:")

for num in range(num_a,num_b+1):
    if num>0 and bin(num).count('1')==4:
        print(num)