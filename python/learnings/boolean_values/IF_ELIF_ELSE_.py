yes = 'yes'
no = 'no'

vegetarian = str(input('are you a vegetarian: '))
vegan = str(input('are you a vegan: '))
gluten_free = str(input('are you a gluten_free: '))

print()

# yes yes yes
if vegetarian == yes and vegan == yes and gluten_free == yes:
    print('Here are the restaurants: ')
    print('Kafe')
    print('Chef')
# no no no
elif vegetarian == no and vegan == no and gluten_free == no:
    print('Here are the restaurants: ')
    print('Hamburger')
    print('Pizza')
    print('Kafe')
    print('Mama')
    print('Chef')
# yes no no
elif vegetarian == yes and vegan == no and gluten_free == no:
    print('Here are the restaurants: ')
    print('Pizza')
    print('Kafe')
    print('Mama')
    print('Chef')
# no yes yes
elif vegetarian == no and vegan == yes and gluten_free == yes:
    print('Here are the restaurants: ')
    print('Kafe')
    print('Chef')
# yes yes no
elif vegetarian == yes and vegan == yes and gluten_free == no:
    print('Here are the restaurants: ')
    print('Kafe')
    print('Chef')
# no no yes
elif vegetarian == no and vegan == no and gluten_free == yes:
    print('Here are the restaurants: ')
    print('Pizza')
    print('Kafe')
    print('Chef')
# no yes no
elif vegetarian == no and vegan == yes and gluten_free == no:
    print('Here are the restaurants: ')
    print('Kafe')
    print('Chef')
# yes no yes
else:
    print('Here are the restaurants: ')
    print('Pizza')
    print('Kafe')
    print('Chef')