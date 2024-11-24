from functools import lru_cache


@lru_cache
def f(n):
    if n == 0: return 0
    return f(n//10) + (n%10)




print((1_134_567_009 - 237_567_899)//10)

# for n in range(1_134_567_008, 1_134_567_009):
#     if f(n) > f(n + 1): 
#         print(f(n), f(n + 1), n)
#         counter += 1

