from random import randint


# random_num = randint(1, 3)

# if random_num == 1:
#     computer_choice = "Камень"
# elif random_num == 2:
#     computer_choice = "Ножницы"
# elif random_num == 3:
#     computer_choice = "Бумага"


variants = ['Камень', "Ножницы", 'Бумага']
computer_choice = variants[randint(0, 2)]

print(computer_choice)