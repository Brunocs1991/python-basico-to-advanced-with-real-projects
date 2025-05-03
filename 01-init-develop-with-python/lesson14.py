a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'a={name1}, b={name2}, c={name3:.2f}'
format_string = string.format(name1=a, name2=b, name3=c)

print(format_string)
