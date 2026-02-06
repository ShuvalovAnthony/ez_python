from string import digits, ascii_uppercase

f = open("Katia/24/23568/24_23568.txt").read()

max_len = 0
first_symb = 0

for i in range(len(f)):
    if f[i] in ascii_uppercase: # f[i] - левая буква
        temp_len = 1

        for j in range(i + 1, len(f)):
            if f[j] in digits:
                temp_len += 1
            else: # f[j] - правая буква
                if f[j] == f[i]:
                    if (temp_len > max_len):
                        max_len = temp_len
                        first_symb = i + 1
                        print(max_len, first_symb, f[i:i+5])
                break


print(first_symb)

print(f.index("V0252"))
