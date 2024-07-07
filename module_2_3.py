my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
while num != len(my_list):
    print(my_list[num])
    num += 1
    if my_list[num] >= 1:
        continue
    elif my_list[num] <= 0:
        num += 1
        continue










