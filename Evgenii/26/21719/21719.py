f = open("Evgenii/26/21719/26_21719.txt")

n = int(f.readline())

students = {}


for row in f:
    id_, task = [int(i) for i in row.split()]

    if id_ in students:
        students[id_].add(task)
    else:
        students[id_] = {task}


def findMaxSolvedTasks(tasks: list):
    max_solved_tasks = 0
    temp_solved_tasks = 1

    for i in range(len(tasks) - 1):
        if tasks[i + 1] - tasks[i] == 2:
            temp_solved_tasks += 1
        else:
            max_solved_tasks = max(max_solved_tasks, temp_solved_tasks)
            temp_solved_tasks = 1

    return max_solved_tasks


min_id = 10**10
max_solved_tasks = 0

for id_, tasks in students.items():
    solved_tasks = findMaxSolvedTasks(sorted(tasks))

    if solved_tasks >= max_solved_tasks:
        max_solved_tasks = solved_tasks
        min_id = min(min_id, id_)


print(min_id, max_solved_tasks)