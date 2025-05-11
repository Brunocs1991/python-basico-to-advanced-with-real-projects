
"""
Write a program that asks the user for the time and, based on the time 
described, displays the appropriate greeting. Ex. 
Good morning 0-11, Good afternoon 12-17 and Good night 18-23.
"""


entry = input('Digite a hora em números inteiros: ')

try:
    hour = int(entry)

    if hour >= 0 and hour <= 11:
        print('Bom dia')
    elif hour >= 12 and hour <= 17:
        print('Bom tarde')
    elif hour >= 18 and hour <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
