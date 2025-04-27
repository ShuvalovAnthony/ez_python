for n in range (3, 10000):
    s = 68 * "9"

    while ("22222" in s) or ("999" in s):
        print (s)
        if ("22222" in s):
            s = s.replace ("22222", "99", 1)
        else:
            s = s.replace ("9999", "29", 1)

    print (s)
    break