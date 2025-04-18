num1 = int( input('Enter number 1 : '))
num2 = int( input('Enter number 2 : '))

# using python's multiple initialisation feature
num1, num2 = num2, num1
# after swapping
print('After swapping : ')
print('Number 1 :',num1)
print('Number 2 :',num2)