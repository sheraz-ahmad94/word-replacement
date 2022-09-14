def replace_word(txt, findWord, replaceWord):
    return str.replace(txt, findWord, replaceWord)

text = 'Hello. This is a string. Replace WORD with something else'
print('\n',text)
fWord = input('\nEnter Word To Replace: ')
rWord = input('Replace With: ')
print('\nNew String: ', replace_word(text, fWord, rWord))