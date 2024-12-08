f = open("17/69927/69927.txt")

data = [int(i) for i in f]



num_of_krat_32 = 0
for i in data:
    num_of_krat_32 += i%32 == 0


counter = 0
max_sum = -10**6


def check(num1, num2):
    return (
        (
            (num1 < 0) or (num2 < 0)
        ) and 
        (
            num1 + num2 < num_of_krat_32
        )
    )


for i in range(len(data) - 1):
    num1, num2 = data[i], data[i + 1]

    if check(num1, num2):
        counter += 1
        max_sum = max(max_sum, num1 + num2)


print(counter, max_sum)