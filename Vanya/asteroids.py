vozrastaet = None # True если возрастает False если убывает
last_num = None
temp_counter = 1


while True:
    n = int(input())

    if n < 0:
        print(temp_counter)
        break
    
    if n < 35:
        print("ALARM")
        break

    if (not last_num) or (n == last_num):
        last_num = n
        continue

    if vozrastaet is None:
        vozrastaet = n > last_num
    
    if (n > last_num): # если текущее число больше предыдущего
        if vozrastaet: # если возрастало
            temp_counter += 1
        else: # если убывало
            print(temp_counter)
            temp_counter = 2
            vozrastaet = True
    else:
        if not vozrastaet:
            temp_counter += 1
        else:
            print(temp_counter)
            temp_counter = 2
            vozrastaet = False
    
    last_num = n