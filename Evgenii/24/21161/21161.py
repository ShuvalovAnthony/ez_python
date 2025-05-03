f = open("Evgenii/24/21161/24_21161.txt").read()


sentensens = f.split(".")


def check(sent: str):
    if not sent: return False
    if sent[0] not in "ABC": return False
    if sent[-1] == ' ': return False
    if '  ' in sent: return False
    for word in sent.split():
        if (len(word) > 1) and (word[1:] != word[1:].lower()): return False
    return True


max_len = 0

for sent in sentensens:
    for i in range(len(sent)):
        temp_sent = sent[i:]
        if check(temp_sent):
            max_len = max(max_len, len(temp_sent) + 1)
            break

print(max_len)