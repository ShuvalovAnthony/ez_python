import pandas as pd

data = {
    'кружок': ['шахматы', 'роботы', 'хор', 'роботы', 'шахматы'],
    'класс': [10, 9, 2, 7, 11],
    'участников': [5, 7, 8, 9, 10],
    'стоимость': [100, 200, 300, 400, 500]
}


df = pd.DataFrame(data)


# for key, value in data.items():
#     print(key, value)

# print(df)

participants = df['участников']

print(participants.mean())
print(participants.sum())












# # clubs = pd.read_csv("https://vebermatvey.neocities.org/courses/data-analysis/notebooks/pandas01_clubs.csv")

# data = {}

# file = open("Egor/pandas/pandas01_clubs.csv")

# for row in file:
#     row = row.replace("\n", "").split(',')

#     title = row[0]
#     col = [int(i) for i in row[1:]]

#     data[title] = col

#     print(data)
#     print()