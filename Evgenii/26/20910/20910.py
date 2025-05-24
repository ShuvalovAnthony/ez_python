f = open("Evgenii/26/20910/26_20910.txt")

n, m, k = [int(i) for i in f.readline().split()]


closest_seats = [m]*(k + 1)

for stroka in f:
    row, seat = [int(i) for i in stroka.split()]
    
    closest_seats[seat] = min(closest_seats[seat], row)


max_row = 0
min_seat = 10**10


for i in range(1, len(closest_seats) - 1):
    left = closest_seats[i]
    right = closest_seats[i + 1]
    closest_seat = min(left, right) - 1

    if closest_seat > max_row:
        max_row = closest_seat
        min_seat = i

print(max_row, min_seat)