f = open("Polina/26/20910/26_20910.txt")


n, max_rows, max_seats = [int(i) for i in f.readline().split()]


v_rows = [10**6]*(max_seats)


for row in f:
    row = [int(i) for i in row.split()]
    v_row, seat = row[1], row[0]

    v_rows[v_row - 1] = min(v_rows[v_row - 1], seat)



closest_seat = 0
answ_row = 10**6


for i in range(len(v_rows) - 1):
    left, right = v_rows[i], v_rows[i + 1]

    if min(left, right) > closest_seat:
        answ_row = i
        closest_seat = min(left, right) - 1


print(closest_seat, answ_row + 1)

