# напишите функцию, которая считает кол-во букв в строке


def countLetters(text: str, letter: str):
    return text.lower().count(letter.lower())


print(countLetters("IUHfnsdfGFSYUDGfbzsuGVFBuysdgvhjbUYFSDVfusydfvgsdfgjhvsdgyuiVBGFSDUYGfvjsh", "G"))