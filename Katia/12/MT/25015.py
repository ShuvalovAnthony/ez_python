from itertools import product


for repeats in range(2, 20):
    for array in product([0, 1], repeat=repeats):
        original_array = list(array)
        array = [5] + list(array) # 5 - лямбда
        

        right_index = len(array) - 1

        while right_index > 0 :
            if array[right_index] == 1: # если в ячейке 1
                array[right_index] = 0 # пишем в нее 0 
                right_index -= 1 # и смещаемся влево
            elif array[right_index] == 0:
                array[right_index] = 1
                right_index -= 1


        res = int(''.join([str(i) for i in array])[1:], 2)
        original_res = int(''.join([str(i) for i in original_array]), 2)
        
        if (res == 320) and (original_array[0] == 1):
            # print(original_array, original_res, array, res)
            print(original_res)
            exit()

