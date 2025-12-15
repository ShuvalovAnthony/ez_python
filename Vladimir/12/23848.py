array = [5] + [0]*155 + [1]*237 + [2]*128 + [3]*480 + [5]


index = 1
state = 1


while True:
    if array[index] == 5 and state == 2:
        break

    if state == 1:
        if array[index] == 5:
            index -= 1
            state = 2
        elif array[index] == 0:
            array[index] = 1
            index += 1
        elif array[index] == 1:
            array[index] = 2
            index += 1
        elif array[index] == 2:
            array[index] = 1
            index += 1
        elif array[index] == 3:
            array[index] = 2
            index += 1

    elif state == 2:
        if array[index] == 1:
            array[index] = 2
            index -= 1
        elif array[index] == 2:
            array[index] = 1
            index -= 1

print(array.count(2))



