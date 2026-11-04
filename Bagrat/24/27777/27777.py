from string import digits, ascii_uppercase

f = open("Bagrat/24/27777/24_27777.txt").read()

alph = digits[1:] + ascii_uppercase[:2]

for digit in (digits + ascii_uppercase):
    if digit not in alph:
        f = f.replace(digit, ' ')

nums = f.split()

print(
    max(
        [len(i) for i in nums]
    )
)