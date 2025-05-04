# Logical operators
# and (and) or (or) not (not)
# or - Any available true condition
# the entire expression as true.
# If any value is considered true,
# the entire expression is analyzed at that value.
# These are considered falsy (which you have already seen)
# 0 0.0 '' False
# There is also the None type which is
# used to represent a non-value

action = input('[IN]Enter [OUT]Exit: ')
password_typed = input('Password: ')

allowed_password = '123456'

if (action == 'IN' or action == 'in') and password_typed == allowed_password:
    print('Enter')
else:
    print('Exit')
print("-" * 50)
# Avaliação de curto circuito
password = input('Senha: ') or 'Empty password'
print(password)
