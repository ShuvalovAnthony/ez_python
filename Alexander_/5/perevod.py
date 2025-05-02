from string import digits, ascii_uppercase as letters

def convert(num: str, from_base, to_base):
    alph = digits + letters

    num = int(num, from_base)

    res = ''

    while num > 0:
        res += alph[num%to_base]
        num //= to_base
    
    return res[::-1]



print(convert("459410937197504318868025558707836643831615", 10, 36))