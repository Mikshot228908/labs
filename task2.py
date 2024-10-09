Temp = float(input("Введите температуру в градусах Цельсия: "))
speed_v = float(input("Введите скорость ветра в метрах в секунду: "))


temp_F = Temp * 9/5 + 32

speed_VM = speed_v / 0.44704

print("Температура в Фаренгейтах:", temp_F)
print("Скорость ветра в милях в час:", speed_VM)

if abs(temp_F) > 50 or speed_VM> 120 or speed_v < 3:
    print("Указанная формула некорректна!")
else:

    w = 35.74 + 0.6215 * temp_F + (0.4275 * temp_F - 35.75) * pow(speed_VM, 0.16)
    w_C = (w - 32) * 5/9
    print("Эффективная температура воздуха в градусах Цельсия:", w_C)
    print("Предупреждение!!!")



