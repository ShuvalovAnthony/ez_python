from string import digits, ascii_uppercase as letters

f = open("Vladimir/24/23568/24_23568.txt").read()

for digit in digits:
    f = f.replace(digit, '*')


res = []

for letter in letters:
    temp_s = f

    for let_to_replace in letters:
        if letter != let_to_replace:
            temp_s = temp_s.replace(let_to_replace, ' ')

    words = temp_s.split()

    for word in words:  
        if (word[0] == word[-1]) and (word.count(letter) == 2):
            res.append([word, f.index(word)])



res = sorted(res, key=lambda x: (-len(x[0]), x[1]))

print(res[0])