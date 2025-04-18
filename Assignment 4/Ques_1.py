# input
testCases = int(input())
loveLetters = [] # list of strings
for _ in range(testCases):
    loveLetters.append(input())
# print(loveLetters)

# logic
# comapare the first letter with last everytime using two pointers

operations = []
for letter in loveLetters: # iterating through each letter one at a time
    i = 0 # starting pointer
    j = len(letter) - 1 # ending pointer
    count = 0 # to count number of operations
    while i <= j: # this ensures entire string is being checked
        start = letter[i]
        end = letter[j]
        while start != end:
            if ord(start) > ord(end):
                start = chr(ord(start) - 1)
            else:
                end = chr(ord(end) - 1)
            count += 1
        i += 1
        j -= 1
    operations.append(count)

for op in operations:
    print(op)