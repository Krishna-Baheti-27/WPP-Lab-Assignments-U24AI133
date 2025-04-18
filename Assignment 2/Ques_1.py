word = input('Enter the word : ')
wordCapitalised = []
i = 0
while i < len(word):
    if i % 2 != 0:
        wordCapitalised.append(word[i].upper())
    else:
        wordCapitalised.append(word[i])
    i += 1

# print
for i in range(len(wordCapitalised)):
    print(wordCapitalised[i],end='')
print() # newline