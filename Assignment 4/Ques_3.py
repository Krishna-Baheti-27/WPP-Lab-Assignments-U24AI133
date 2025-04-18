# input
num = input()

#logic
#creating all alphabet list of lower case alphabets
alphabets = []
alphabetCount = [0] * 26 # to count occurences of alphabets
ch = 'a'
for i in range(26):
    alphabets.append(chr( ord(ch) + i))

for i in range(len(num)):
    for j in range(26):
        if num[i].lower() == alphabets[j]:
           alphabetCount[j] += 1
           break

# checking 
checkPangram = True

for i in range(26):
    if alphabetCount[i] == 0:
        print('not pangram')
        checkPangram = False
        break

if checkPangram == True:
    print('pangram')
