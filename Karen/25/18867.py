# def check(num: int): # 33?2*42?
#     num = str(num)

#     return (
#         (num[2] in "02468") and 
#         (num[-1] in "02468") and
#         (num[:2] == "33") and
#         (num[3] == "2") and
#         (num[-3:-1] == "42")
#     )

from fnmatch import fnmatch

for num in range(2025, 10**10, 2025):
    if fnmatch(str(num), "33?2*42?") and fnmatch(str(num), "*32??2?"):
        print(num, num//2025)
