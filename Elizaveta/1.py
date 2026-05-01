# typecasting

# age = int(input("Input the age")) # str

# if age > 18:
#     print("Adult")
# else:
#     print("Underage")


# print(10/2) # / -> float

# 5.0


# marks = int(input("whats your score out of 100 "))


# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")



# year = int(input())

# if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#     print("Leap year")


# for num in range(1, 20, 2):
#     print(num)


# for num in range(13, 100, 13):
#     print(num)

# infinity loop

# find an mean/average of a set of non zero numbers


# a = 1

# while a < 10:
#     print(a)
#     a = a + 1 # a += 1 - increment by 1


# summ = 0
# count = 0

# while True:
#     num = int(input())

#     # condition to interrupt loop
#     if num == 0:
#         break

#     summ += num # summ = summ + num
#     count += 1

# print(summ/count)


# 5, 8, 9, 4, 1, 0 - avg = 5.4

# collections: string "fsdfds", list [1, 2, 3]
# range() - generator

# nums = [5, 8, 9, 4, 1]

# for i in nums:
#     print(i)


# nums = [5, 8, 9, 4, 1]
# summ = 0
# count = 0

# for num in nums:
#     summ += num
#     count += 1

# print(summ/count)


# print(sum(nums)/len(nums)) # нельзя!



# find max/min

# nums = [5, 8, 9, 4, 1]

# max = 0

# for i in nums:
#     if i > max:
#         max = i

# print(max)



# nums = [5, 8, 9, 4, 1]

# min = 10**10

# for i in nums:
#     if i < min:
#         min = i

# print(min)



nums = [5, 8, 9, 4, 1]

# value = int(input())
value = 9

for i in nums:
    if value == i:
        print("END")





# a = 20

# while a <= 36:
#     print(a)

#     a = a + 3


# # start - included
# # stop - excluded
# # step
# print('----')
# for a in range(20, 37, 3):
#     print(a)





# for i in range(44, 20, -5):
#     print(i)



# a = 44

# while a > 20:
#     print(a)

#     a = a - 5