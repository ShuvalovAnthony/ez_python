index = 1

for a1 in sorted('ВЕСНА'):
    for a2 in sorted('ВЕСНА'):
        for a3 in sorted('ВЕСНА'):
            for a4 in sorted('ВЕСНА'):
                word = a1 + a2 + a3 + a4
                

                if word.count('Е') == 0 and word.count('АА') == 0:
                    print(index,word)


                index += 1
