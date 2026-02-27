f = open("Katia/17/68279/17.txt")

nums = [int(i) for i in f]


max_na_562 = max([i for i in nums if str(i)[-3:] == "562"])


def check(row: list):
    pyat = [i for i in row if i in range(10_000, 100_000)]
    nepyat = [i for i in row if i not in range(10_000, 100_000)]
    krat_3 = [i for i in row if i%3 == 0]
    krat_7 = [i for i in row if i%7 == 0]

    return (
        (len(pyat) >= 1) and
        (len(nepyat) >= 2) and
        (len(krat_3) < len(krat_7)) and
        (max_na_562 < sum(row) < max_na_562*2)
    )


counter = 0
max_summa = 0


for i in range(len(nums) - 3):
    row = nums[i: i + 4]

    if check(row):
        counter += 1
        max_summa = max(max_summa, sum(row))

print(counter, max_summa)