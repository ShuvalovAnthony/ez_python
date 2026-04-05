from time import sleep

f = open("Mihail/26/kino/data.txt")


n = int(f.readline()) # колво рядов
m = int(f.readline()) # колво мест в ряду

closest_seats = [n]*(m + 3)


for line in f:
    row, seat = [int(i) for i in line.split()]

    closest_seats[seat] = min(closest_seats[seat], row)
    print(closest_seats, f"dobavleno mesto{seat} v ryadu {row}")
    sleep(5)

