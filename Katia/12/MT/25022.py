original_array = [0]*45 + [1]*21

array = [5] + original_array


right_index = len(array) - 1

state = 1

while right_index != 0:
    if state == 1:
        if array[right_index] == 1:
            array[right_index] = 0
            state = 3
            right_index -= 1
        elif array[right_index] == 0:
            array[right_index] = 1
            state = 2
            right_index -= 1

    elif state == 2:
        if array[right_index] == 1:
            array[right_index] = 0
            state = 1
            right_index -= 1
        elif array[right_index] == 0:
            state = 3
            right_index -= 1
    
    elif state == 3:
        if array[right_index] == 1:
            state = 2
            right_index -= 1
        elif array[right_index] == 0:
            array[right_index] = 1
            state = 1
            right_index -= 1

print(array.count(0))



