# taking input
num = float( input('Enter a length in feet : '))


# creating list to store all conversions
unitConveter = [
    num * 12,             # 1 foot = 12 inches
    num / 3,           # 1 foot = 1/3 yards
    num / 5280,        # 1 foot = 1/5280 miles
    num * 304.8,    # 1 foot = 304.8 millimeters
    num * 30.48,    # 1 foot = 30.48 centimeters
    num * 0.3048,        # 1 foot = 0.3048 meters
    num * 0.0003048  # 1 foot = 0.0003048 kilometers
]

print()
print('------------------------- MENU ----------------------------')
print('Enter 1 to convert to inches')
print('Enter 2 to convert to yards')
print('Enter 3 to convert to miles')
print('Enter 4 to convert to millimeters')
print('Enter 5 to convert to centimeters')
print('Enter 6 to convert to meters')
print('Enter 7 to convert to kilometers')
print('------------------------ END ------------------------------')

choice = int( input('Enter the choice : '))
print(unitConveter[choice-1])

