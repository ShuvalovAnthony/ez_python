n = 9

results = {40: {3, 4}, 60: {33}, 50: {72, 125, 126, 127}}


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




nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


a0 = 0
a1 = 1
a2 = 2