# напишите функцию, которая считает кол-во букв в строке


# def countLetters(text: str, letter: str):
#     return text.lower().count(letter.lower())


# print(countLetters("IUHfnsdfGFSYUDGfbzsuGVFBuysdgvhjbUYFSDVfusydfvgsdfgjhvsdgyuiVBGFSDUYGfvjsh", "G"))


# comment = ctr + /
# tab == ctrl + ]
# reverse tab = ctrl + [


def prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True
