# PART 1
list1 = [0] * 50
for i in range(50):
    list1[i] = i;
print(list1)
print()

# PART 2
list2 = [0] * 50
for i in range(50):
    list2[i] = (i+1) ** 2
print(list2)
print()

# PART 3
list3 = [''] * 26
for i in range(26):
    ch = chr( ord('a') + i)
    for j in range(i+1):
        list3[i] += ch
print(list3)
print()