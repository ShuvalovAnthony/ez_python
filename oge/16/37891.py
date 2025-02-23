n = int(input())

kolichestvo_ne_sdavshih = 0
perfect = False

for _ in range(n):
    kolvo_vernih = int(input())
    if kolvo_vernih < 5:
        kolichestvo_ne_sdavshih += 1
    
    if kolvo_vernih == 10:
        perfect = True


print(kolichestvo_ne_sdavshih)

if perfect: print("YES")
else: print("NO")

