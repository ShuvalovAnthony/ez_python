for p in range(37):
    try:
        res = (
            int("17496", p) +
            int("91F83", p) +
            int("D9543", p)
        )

        if res%12 == 0:
            print(res//12)
    except:
        ...