array = [1]*750 + [0]*650 + [2]

index = 0
state = 0


while True:
    if state == 0:
        if array[index] == 0:
            array[index] = 1
            index += 1
            state = 1
        elif array[index] == 1:
            array[index] = 0
            index += 1
            state = 1
        elif array[index] == 2:
            array[index] = 1
            break
    elif state == 1:
        if array[index] == 0:
            array[index] = 1
            index += 1
            state = 0
        elif array[index] == 1:
            array[index] = 0
            index += 1
            state = 0
        elif array[index] == 2:
            array[index] = 0
            break

print(array.count(1))