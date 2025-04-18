# d = open('1')
# h=[]
# for j in d:
#     k=1
#     m=0
#     for a,b in zip(j,j[1:]):
#         if a==b:
#             k+=1
#         else:
#             if k>m:
#                 m=k
#                 g=a
#             k=1
#     h.append([m,j.count(g),g])
# h.sort()
# print(h[-1])



# b = open("24").read()
# i = 0
# k = 0
# mx = 0
# g = ["A", "O"]
# while i < len(b):
#     if b[i] not in g and b [i+1] in g:
#         k += 2
#         i += 2
#     else:
#         mx = max(k, mx)
#         k = 0
#         i += 1
# print(k)


# d = [i for i open("24")]
# mn = 100000
# for j in range(len (d)):
#     if d[j].count("N") < mn:
#         mn = j.count("N")
#         mn = d[j].count("N")
# b = d[i]
# mx = 0
# for j in "ASBCDEFGHIJKLMNOPQRISTUVWXYZ":
#     if b.count(j) >= mx:
#         mx = b.count(j)
#         k = j
# print(k)