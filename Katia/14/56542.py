from string import digits, ascii_uppercase

alph = digits + ascii_uppercase



for p in range(10, 36): # p = 10
    for x in alph:
        for y in alph:
            try:    
                if (
                    int("32" + x + "8", p) + int(x*3 + "9", p) ==
                    int(y*2 + "02", p)
                ):
                    print(int(y + y + x, p))
            except:
                ...
                    
