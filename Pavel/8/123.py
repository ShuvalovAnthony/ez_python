from itertools import product

index = 1

for word in product(sorted ("МИЗАНТРОП"), repeat = 5):
      word = ''.join(word)

      if (
              (word[0] == 'Н') and
              (word.count('Р') == 2) and
              (index % 2 == 0)
      ):
           print(index)

      index += 1