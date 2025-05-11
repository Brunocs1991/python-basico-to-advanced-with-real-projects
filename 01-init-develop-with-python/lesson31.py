
"""
Flag - Mark a location
None = No value
is and is not = is or is not (type, value, identity)
id = Identity
"""
condition = False
pass_in_if = None

if condition:
    pass_in_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if pass_in_if is None:
    print('Não passou no if')
else:
    print('Passou no if')