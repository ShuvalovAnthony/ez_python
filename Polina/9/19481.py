def check(row: list):
    sorted_row = sorted(row)

    return (
        (len(row) == len(set(row))) and
        ((sorted_row[0] + sorted_row[-1])**2 > sum([i**3 for i in sorted_row[1:-1]]))
    )

