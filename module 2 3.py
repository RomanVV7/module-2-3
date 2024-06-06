my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
while len(my_list) <= 12:
    if my_list[zero] > 0:
        print(my_list[zero])
        zero = zero + 1
        if my_list[zero] == 0:
            zero = zero + 1
            continue
    else:
        break
