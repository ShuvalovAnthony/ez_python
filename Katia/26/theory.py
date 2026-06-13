# data = [
#     # ID 4⬆️, Матем 2⬇️, Рус 3⬇️, Инф 1⬇️
#     [1001, 70, 70, 85],
#     [995, 70, 90, 80],
#     [992, 70, 92, 80,],
#     [1002, 60, 100, 90],
#     [1007, 70, 70, 85],
# ]



# data = sorted(data, key=lambda el: [
#     -sum(el[1:]),
    
# ])


# for row in data:
#     print(*row)




# passed = [
#     [1, 100, 5],
#     [4, 99, 2],
#     [112, 98, 3],
#     [332, 97, 7],
#     [444, 97, 10],
# ]


# failed = [
#     [555, 97, 1],
#     [666, 97, 2],
#     [11, 96, 7],
#     [22, 80, 10],
# ]


# for row in failed:
#     if row[1] == passed[-1][1]:
#         passed.append(row)
#         failed = failed[1:]



# for row in failed:
#     print(row)


message = {
  
  "chats": {
    "about": "This page lists all chats from this export.",  
    "list": [
      {  
        "name": "Somebody",  
        "type": "personal_chat",  
        "id": 4295744296,
        "messages": [
           {
            "id": 642,
            "type": "message",
            "date": "2018-10-09T19:32:23",
            "from": "Julie Ducasse",
            "from_id": 653911985,
            "text": "Hello :) !"
           }
          ]
      }
     ]
  },
  "about": "Here is the data you requested. ...",  
}

# print(message["chats"]["list"][0]["messages"])





data = {}

data[55] = [1, 2, 3]
data[22] = [1, 2, 3, 4, 5]
data[77] = [6]
data[22].append(99)


if 77 in data:
    data[77].append(77)
else:
    data[77] = [5]

for row, seats in data.items():
    print(row, seats)