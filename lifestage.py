# Ask the age to the user
t = int(input('What is your age? '))

# Check and print the lifestage for different ages
if t < 2:
    print('Baby')
elif t < 4:
    # Don't need to use 2 here again, since that is alredy checked
    print('Toddler')
elif t < 13:
    print('Kid')
elif t < 20:
    print('Teenager')
elif t < 65:
    print('Adult')
else:
    print('Elder')