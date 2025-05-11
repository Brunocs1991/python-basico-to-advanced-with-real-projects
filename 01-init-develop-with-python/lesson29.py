"""
Introduction to try/except
try -> try to execute the code
except -> an error occurred while trying to execute
"""

number_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    number_float = float(number_str)
    print('FLOAT:', number_float)
    print(f'O dobro de {number_str} é {number_float * 2:.2f}')
except:
    print('Isso não é um número')