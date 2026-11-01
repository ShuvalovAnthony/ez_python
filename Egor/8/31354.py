from itertools import product
index=1
answer=[]
for word in product(sorted('СОЛНЦЕ'), repeat=6):
    word=''.join(word)
    if (index%2!=0 and word[0] not in "ЦН" and
        word.count('Ц')==1 and word.count('Н')==1):
        answer.append(index)
    index+=1
print(max(answer))
