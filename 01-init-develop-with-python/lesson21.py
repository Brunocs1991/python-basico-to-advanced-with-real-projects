# Logical operators
# and (and) or (or) not (not)
# and - All conditions must be
# true.
# If any value is considered false,
# the entire expression will be evaluated at that value
# They are considered falsy (which you have already seen)
# 0 0.0 '' False
# There is also the None type which is
# used to represent a non-value
action = input('[IN]Enter [OUT]Exit: ')
password_typed = input('Password: ')

allowed_password = '123456'

if action == 'IN' and password_typed == allowed_password:
    print('Enter')
else:
    print('Exit')
print("*" * 20)
# Short-circuit evaluation
print(True and False and True)
print(True and 0 and True)
