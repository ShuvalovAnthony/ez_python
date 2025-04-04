f = open("Daniil/27/68258/1_27_B.txt")

n = int(f.readline())

komplekti = [int(i) for i in f]

print(len(komplekti))

min_summa = 10**6

for i in range(len(komplekti)):
    temp_summa = 0
    
    right = (komplekti*2)[i + 1:i + n//2 + 1]
    left = (komplekti*2)[i + n//2 + 1:i + n][::-1]

    # right side
    for j in range(len(right)):
        temp_summa += (j + 1)*right[j]
    
    # left side
    for j in range(len(left)):
        temp_summa += (j + 1)*left[j]

    if temp_summa < min_summa:
        min_summa = temp_summa


print(min_summa)

