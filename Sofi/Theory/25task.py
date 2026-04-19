# def deliteli(num):
#     dels = set()

#     for delit in range(2, int(num**0.5) + 1):
#         if num%delit == 0:
#             dels.add(delit)
#             dels.add(num//delit)

#     return sorted(dels)

# def sumMinAndMaxDivs(num):
#     for delit in range(2, int(num**0.5) + 1):
#         if num%delit == 0:
#             return delit + num//delit


# print(sumMinAndMaxDivs(100))