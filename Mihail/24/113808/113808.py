f = open("Mihail/24/113808/24_5.txt").read()

for i in ['+', "**", "*0*", "*0"]:
    f = f.replace(i, ' ')

nums = sorted(f.split(), key=lambda x: -len(x))

for num in nums[:30]:
    num = num.lstrip("0").strip("*")
    print(num, str(eval(num))[-10:])



# valid = []

# temp_num = ''


# for i in range(len(f)):
#     if not temp_num:
#         if f[i] in '0123456789':
#             temp_num += f[i]
#     else:
#         if f[i] == "+":
#             if temp_num[-1] == "*":
#                 # print(temp_num[:-1])
#                 valid.append(temp_num[:-1])
#             else:
#                 # print(temp_num)
#                 valid.append(temp_num)
#             temp_num = ''
        
#         elif temp_num[-1] == '0' and len(temp_num) == 1:
#             if f[i] == "*":
#                 temp_num += f[i]
#             else:
#                 temp_num = ''

#         # *0
#         elif temp_num[-1] == '0':
#             if temp_num[-2] == "*":
#                 if f[i] == "*":
#                     temp_num += f[i]
#                 else:
#                     valid.append(temp_num)
#                     temp_num = ''
            
#         elif temp_num[-1] == "*":
#             if f[i] == "*":
#                 # print(temp_num[:-1])
#                 valid.append(temp_num[:-1])
#                 temp_num = ''
#             else:
#                 temp_num += f[i]
#         else:
#             temp_num += f[i]

    
    
# valid = sorted(valid, key=lambda x: -len(x))      

# # for num in valid[:20]:
# #     print(num)

# def getMaxMult(num: str):
#     res = []
#     nums = num.split("*")

#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             temp_nums = nums[i: j + 1]
#             temp_res = 1

#             for n in temp_nums:
#                 temp_res *= int(n)

#             res.append(temp_res)
#     if res:
#         return max(res)
#     return 0



# # results = [getMaxMult(i) for i in valid]

# # print(max(results))

