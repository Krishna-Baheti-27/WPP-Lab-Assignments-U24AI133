# use slice(15) to reduce the length og input string to fifteen characters
# use [::-1] to reverse a given string in python


print('Enter the names of students (10 in total) : ')
print()
list1 = [''] * 10
display_list = []
for i in range(10):
    list1[i] = input(f'Enter the name of student {i+1} : ')
    if len(list1[i]) <= 15:
        display_list.append(list1[i] [::-1])
    else:
        display_list.append( list1[i][slice(15)] [::-1])
        
print(display_list)

