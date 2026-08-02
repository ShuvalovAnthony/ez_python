def mnozh(num):
    res = set()

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0 :
            # i - первый множитель
            # num//i - второй множ
            res.add(i)
            res.add(num//i)

    return [max(res), min(res)]



print(mnozh(3422554353456723))