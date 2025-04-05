# largest = int(input())
# medium = int(input())
# smallest = int(input())

# if largest >= medium >= smallest:
#     largest, medium, smallest = largest, medium, smallest
# elif largest >= smallest >= medium:
#     largest, medium, smallest = largest, smallest, medium
# elif medium >= largest >= smallest:
#     largest, medium, smallest = medium, largest, smallest
# elif medium >= smallest >= largest:
#     largest, medium, smallest = medium, smallest, largest
# elif smallest >= largest >= medium:
#     largest, medium, smallest = smallest, largest, medium
# elif smallest >= medium >= largest:
#     largest, medium, smallest = smallest, medium, largest

# print(largest)
# print(medium)
# print(smallest)


largest, medium, smallest = sorted([int(input()), int(input()), int(input())], reverse=True)
print(largest)
print(medium)
print(smallest)