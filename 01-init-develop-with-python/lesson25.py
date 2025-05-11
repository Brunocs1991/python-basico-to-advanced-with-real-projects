"""
Basic string interpolation
s - string
d and i - int
f - float
x and X - Hexadecimal (ABCDEF0123456789)
"""
name = 'Luiz'
price = 1000.95897643
variable = '%s, o preço é R$%.2f' % (name, price)
print(variable)
print('O hexadecimal de %d é %08X' % (1500, 1500))
