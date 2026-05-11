f = open("Mihail/17/25725/17_25725.txt")

nums = [int(i) for i in f]

count = len([i for i in nums if abs(i)%3 == 0])

def check(pair: list):
    return (
        (
            (pair[0] < 0 and abs(pair[1])%2 == 0) or 
            (pair[1] < 0 and abs(pair[0])%2 == 0)
        ) and
        (sum(pair) > count)
    )


counter = 0
max_sum = 0

for i in range(len(nums) - 1):
    pair = nums[i: i + 2]

    if check(pair):
        print(pair)
        counter += 1
        max_sum = max(max_sum, sum(pair))


print(counter, max_sum)


# f = open(r"Mihail/17/25725/17_25725.txt")
# data = [int(i) for i in f]
# count = len([int(i) for i in data if abs(i) % 3 == 0])
# print(count)
# def check(pari: list):
#     k1 = ([int(i) for i in pari if i < 0])
#     k2 = ([int(i) for i in pari if i % 2 == 0])
#     summa = sum(int(i) for i in pari)
#     if k1 and k2:
#         return (len(k1) == 1 and len(k2) == 1 and k1[0] != k2[0]) and summa > count

# k = 0
# spisok = []
# for i in range(len(data) -1):
#     pari = data[i:i+2]
#     if check(pari):
#         k += 1
#         spisok.append(sum(pari))
#         print(pari)
# print(k, max(spisok))