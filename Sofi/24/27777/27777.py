from string import ascii_uppercase

f = open("Sofi/24/27777/24_27777.txt").read()


for letter in ascii_uppercase:
    if letter not in "AB":
        f = f.replace(letter, ' ')


print(
    max([len(i) for i in f.split()])
)