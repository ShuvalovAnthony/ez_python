from string import digits, ascii_uppercase


f = open('Katia/sandbox/data.txt').read()

alph = digits + ascii_uppercase[:14]
for let in set(f):
    if let not in alph:
        f = f.replace(let, " ")


print(max(len(i.lstrip('0')) for i in f.split()))