start = int(input())
stop = int(input())

for num in range(start, stop + 1):
    num = str(num)
    if len(set(num)) == len(num):
        print(num)