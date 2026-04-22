from string import punctuation

f = open("Danya/10/28756/28756.txt").read().lower()

for i in punctuation:
    f = f.replace(i, '')

counter = 0

for word in f.split():
    if ("то" in word) and (len(word) > 2):
        counter += 1




print(counter)


