
"""
Write a program that asks for the user's first name. If the name has 4 letters or 
less, write "Your name is short"; if it has between 5 and 6 letters, write 
"Your name is normal"; if it has more than 6 letters, write "Your name is too long".
"""
name = input('Digite seu nome: ')
name_len = len(name)

if name_len > 1:
    if name_len <= 4:
        print('Seu nome é curto')
    elif name_len >= 5 and name_len <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
