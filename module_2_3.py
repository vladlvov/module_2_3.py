my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while 0 < len(my_list):
    numbers = int(my_list[i])
    i += 1
    if numbers >= 1:
        print(numbers)
    elif numbers == 0:
        continue
    else:
        break
