f = open("Evgenii/24/16388/24_16388.txt").read()


for i in range(100, 0, -1):
    if "KLMN"*i in f:
        max_groups = i
        break


starts = ["LMN", "MN", "N", '']
ends = ["KLM", "KL", "K", '']


for start in starts:
    for end in ends:
        s = start + max_groups*"KLMN" + end
        if s in f:
            print(len(s))
            