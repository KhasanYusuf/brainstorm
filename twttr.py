ban='aiueoAIUEO'
word=input('')
for letter in word:
    if letter in ban:
        word=word.replace(letter,'')
print(word)