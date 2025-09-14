# range(start, stop, step)

# start - входит
# stop - НЕ ВХОДИТ!!!!!


for num in range(10, 100): # двузначные
    if (
        (num//10%2 == 1) and (not num%3 == 0)
    ):
        print(num)