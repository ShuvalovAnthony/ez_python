f = open("Alexander/26/19256/26_19256.txt")

n = int(f.readline())

results = {}


for row in f:
    id_, task = [int(i) for i in row.split()]
    
    if id_ in results:
        results[id_].add(task)
    else:
        results[id_] = {task}


def findMaxSolvedTasks(tasks: set):
    tasks = sorted(tasks)

    max_solved_tasks = 0
    temp_solved_tasks = 1

    for i in range(len(tasks) - 1):
        if tasks[i] == tasks[i + 1] - 1:
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
        res_id = min(res_id, id_)

print(res_id, max_solved_tasks)