# переменные
a = 16

print(a**0.5)

# убрать из текста все плохие слова

text = input()
bad_words = ['abc', 'ABC', "aaa"]

for bad_word in bad_words:
    text = text.replace(bad_word, '')

print(text)