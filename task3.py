isb_n9 = input("Введите первые 9 цифр ISBN:")

if len(isb_n9) != 9 or not isb_n9.isdigit():
    print("Error!!!!")
else:
    total = 0
    for i in range(9):
        total += (10 - i) * int(isb_n9[i])

    remainder = total % 11
    check_num = 11 - remainder

    if check_num == 10:
        check_num = '10'
    elif check_num == 11:
        check_num = '0'
    else:
        check_num = str(check_num)

    isb_n10 = isb_n9 + check_num

    print(f"Полный ISBN-10: {isb_n10}")
