"""
Write a program that asks the user to enter an integer,
and informs whether this number is even or odd. If the user does not enter an integer,
inform that it is not an integer.
"""
entry = input('Digite um número: ')

if entry.isdigit():
    entry_int = int(entry)
    par_impar = entry_int % 2 == 0
    par_impar_text = 'ímpar'

    if par_impar:
        par_impar_text = 'par'

    print(f'O número {entry_int} é {par_impar_text}')
else:
    print('Você não digitou um número inteiro')

try:
    entry_int = float(entry)
    par_impar = entry_int % 2 == 0
    par_impar_text = 'ímpar'

    if par_impar:
        par_impar_text = 'par'

    print(f'O número {entry_int} é {par_impar_text}')
except:
    print('Você não digitou um número inteiro')
