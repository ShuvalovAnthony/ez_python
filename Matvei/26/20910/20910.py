f = open("Matvei/26/20910/26_20910.txt")

n, m, k = [int(i) for i in f.readline().split()]

# m - рядов k - мест в ряду

v_rows = [m]*(k + 1)


for i in f:
    row, v_row = [int(j) for j in i.split()]
    
    v_rows[v_row] = min(v_rows[v_row], row)

max_closest_row = 0
min_left_seat = 10**10

for i in range(1, len(v_rows) - 1):
    left = v_rows[i]
    right = v_rows[i + 1]
    closest_row = min(left, right) - 1

    if closest_row > max_closest_row:
        max_closest_row = closest_row
        min_left_seat = i

print(max_closest_row, min_left_seat)

