dict = {} # empty dictionary

# taking input
choice = 'break'
while True:
    print(choice)
    choice = input('Enter "break" to stop entering or enter the Product Name : ')
    if choice == "break":
        break
    else:
        productPrice = input('Enter its price : ')
        dict.update({choice: productPrice})

# printing as per user request
while True:
    choiceAgain = input('Enter "break" to stop entering or enter the Product Name (to get price) : ')
    if choiceAgain == 'break':
        break
    if choiceAgain in dict:
        print('Product price :',dict.get(choiceAgain))
    else:
        print('Product not found\n')
