f = open("Vladimir/24/6798/24_6798.txt").read()

# Текстовый файл состоит из символов A, C, D, F и O. 
# Определите максимальное количество идущих подряд троек символов вида
#   согласная + любая буква + гласная


f = f.replace("O", "A").replace("F", "C").replace("D", "C").replace("CCA", "QWE").replace("CAA", "QWE")


for i in range(10**6):
    if "QWE"*i in f:
        print(i)
    else:
        break

