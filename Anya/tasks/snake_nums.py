num_of_cols = int(input())
num_of_rows = int(input())

num_of_cols, num_of_rows = max(num_of_cols, num_of_rows), min(num_of_cols, num_of_rows)

print(num_of_cols, num_of_rows)

for row in range(1, num_of_rows + 1):
    if row%2 == 1:
        for col in range(
            1 + num_of_cols * (row - 1), 
            1 + num_of_cols * (row - 1) + num_of_cols
        ):
            print(col, end="\t")
    else:
        for col in range(
            num_of_cols * (row - 1) + num_of_cols,
            num_of_cols * (row - 1),
            -1
        ):
            print(col, end="\t")

    print()