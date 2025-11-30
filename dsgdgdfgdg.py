products = ['apple', 'orange', 'cucumber', 'tomato', 'potato', 'grape', 'strawberry']

fruits = []
vegetables = []
berries = []

other = []

for product in products:
    print("1 - fruits, 2 - vegetables, 3 - berries, 4 - other for", product.upper())
    choice = int(input())

    if choice == 1:
        fruits.append(product)
    elif choice == 2:
        vegetables.append(product)
    elif choice == 3:
        berries.append(product)
    else:
        other.append(product)


print("Fruits", *fruits)
print("Vegetables", *vegetables)
print("Berries", *berries)
print("Other", *other)

name = "Eduard Bakero-Fernandes Maksimovich" # max lenght?