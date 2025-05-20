f = open("Matvei/26/21719/26_21719.txt")

n = int(f.readline())

results = {}

for row in f:
    id_, task = [int(i) for i in row.split()]

    if task%2 == 0:
        if (str(id_) + "chet") in results:
            results[str(id_) + "chet"].add(task)
        else:
            results[str(id_) + "chet"] = {task}
    else:
        if (str(id_) + "nech") in results:
            results[str(id_) + "nech"].add(task)
        else:
            results[str(id_) + "nech"] = {task}


def findMaxSolvedTasks(tasks: set):
    tasks = sorted(tasks)
    max_solved_tasks = 0
    temp_solved_tasks = 1

    for i in range(len(tasks) - 1):
        if tasks[i] == tasks[i + 1] - 2:
            temp_solved_tasks += 1
        else:
            max_solved_tasks = max(max_solved_tasks, temp_solved_tasks)
            temp_solved_tasks = 1

    return max(max_solved_tasks, temp_solved_tasks)



res_id = 10**10
max_solved_tasks = 0


for id_, tasks in results.items():
    solved_tasks = findMaxSolvedTasks(tasks)

    if solved_tasks >= max_solved_tasks:
        max_solved_tasks = solved_tasks
        res_id = min(res_id, int(id_[:-4]))


print(res_id, max_solved_tasks)

