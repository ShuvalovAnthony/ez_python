def convert(num: str, from_base: int, to_base: int):
    """2 <= bases <= 36"""
    from string import digits, ascii_uppercase

    alph = digits + ascii_uppercase

    dec_num = int(str(num), from_base)

    res = ''

    while dec_num > 0:
        res += alph[dec_num%to_base]
        dec_num //= to_base

    return res[::-1]

