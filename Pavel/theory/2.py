# # while for 
# from string import digits, ascii_uppercase

# alph = digits + ascii_uppercase[:6]
# print(alph)

# n = 2555

# digits = ""

# while n > 0:
#     digits += alph[n%16]
#     n //= 16

# digits = digits[::-1]

# print(digits.count("F"))

# print(digits.count(15))


# nums = [-5, 8, 9, 11, -90, 101, 1]
#         # 0 1  2  3   4    5    6

# for i in range(len(nums) - 1): # 0 1 2 3 4 5 6
#     print(nums[i], nums[i + 1])

# for num in nums:
#     print(num)

# print(nums[2:6])


text = "fiudhg nfdjgkh nuhg dfuig hdfiguhfdgn iudfkgjhduifl gdfn gjkdfn gljkdfng dfjlkgn dfgjklndf gjkldf"
text_2 = "gdf iujnjk gjdfkbg dfgdfg"
text_3 = "fsd asfs ferggdfg"



def find_longest_word_in_text(text):
    words = text.split()

    longest_word = ''

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word



def filter(text: str, banned_words: list):
    for word in banned_words:
        text = text.replace(word, '#%!_*')
    
    return text


print(filter("Abc abc fff fsdkjf sfk ttt ttt ttt sdflksndkf fff dsflsndf sdfn fff", ['fff', 'ttt']))