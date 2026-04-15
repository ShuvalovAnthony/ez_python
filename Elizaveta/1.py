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

nums = [5, 8, 9, 4, 1]



summ = 0
count = 0

for num in nums:
    summ += num
    count += 1

print(summ/count)


# print(sum(nums)/len(nums)) # нельзя!