array = [1]*30 + [0]*45 + [5] # 5 - лямбда


state = 1

left_index = 0

while array[left_index] != 5:
    if state == 1:
        if array[left_index] == 1:
            state = 2
            left_index += 1
        elif array[left_index] == 0:
            state = 2
            left_index += 1
    elif state == 2:
        if array[left_index] == 1:
            array[left_index] = 0
            state = 3
            left_index += 1
        elif array[left_index] == 0:
            array[left_index] = 1
            state = 3
            left_index += 1
    elif state == 3:
        if array[left_index] == 1:
            state = 1
            left_index += 1
        elif array[left_index] == 0:
            state = 2
            left_index += 1

print(array.count(1))