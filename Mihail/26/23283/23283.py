f = open("Mihail/26/23283/26_23283.txt")

k = int(f.readline()) # kolvo okon
n = int(f.readline()) # kolvo customerov

time_stamps = [
    [int(i) for i in row.split()] for row in f
]

time_stamps = sorted(time_stamps, key=lambda x: (
    x[0],
    x[1],
))

windows = {
    i: [] for i in range(1, k + 1) # [101, 187, 255 - время освобождения окна (stop)]
}


def sendToWindow(start, stop):
    for winNum, queue in windows.items():
        if not queue:
            queue.append(stop)
            return winNum
        if start >= queue[-1] + 1:
            queue.append(stop)
            return winNum
    return False


counter = 0
last_window = None


for start, stop in time_stamps:
    func_res = sendToWindow(start, stop)
    if func_res:
        counter += 1
        last_window = func_res


print(counter, last_window)